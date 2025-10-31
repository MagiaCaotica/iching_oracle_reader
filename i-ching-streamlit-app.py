# -*- coding: utf-8 -*-
import streamlit as st
import random
import matplotlib.pyplot as plt
import time
from data import HEXAGRAM_DATA

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Digital I-Ching Oracle",
    page_icon="☯️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Estilos CSS Personalizados ---
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #e6e6e6;
    }
    .stButton>button {
        border: 2px solid #e6e6e6;
        border-radius: 20px;
        color: #e6e6e6;
        background-color: transparent;
        padding: 10px 24px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        border-color: #c4a748;
        color: #c4a748;
    }
    .stTextArea>div>textarea {
        background-color: #333333;
        color: #e6e6e6;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #c4a748; /* Un tono dorado/ocre */
    }
    blockquote {
        color: #b3b3b3;
        border-left: 5px solid #c4a748;
        padding-left: 1rem;
        margin-left: 0;
        font-style: italic;
    }
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
    }
    .centered-text {
        text-align: center;
    }
    .qr-code {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* --- Media Queries para Responsividad --- */
    @media (max-width: 768px) {
        /* Hacer que las columnas de los hexagramas se apilen verticalmente */
        div[data-testid="stHorizontalBlock"] {
            flex-direction: column;
        }

        /* Ajustar el tamaño de la fuente para una mejor legibilidad en móviles */
        h1 {
            font-size: 28px;
        }
        h2 {
            font-size: 24px;
        }
        h3 {
            font-size: 20px;
        }
        .stButton>button {
            padding: 8px 18px;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Lógica del I-Ching ---

@st.cache_data
def load_hexagram_data():
    """Carga y mapea los datos de los hexagramas para una búsqueda rápida."""
    return {h["binary"]: h for h in HEXAGRAM_DATA} # No changes needed here

HEXAGRAMS_BY_BINARY = load_hexagram_data()

def throw_coins():
    """Simula el lanzamiento de 3 monedas para obtener un valor de línea (6, 7, 8, o 9)."""
    return sum(random.choice([2, 3]) for _ in range(3)) # Cara=3 (Yang), Cruz=2 (Yin)

def get_line_properties(value):
    """Determina las propiedades de una línea a partir de su valor numérico."""
    if value == 6: # Yin mutable
        return {"type": "Yin", "is_changing": True, "binary": 0, "symbol": "--- X ---"}
    elif value == 7: # Yang estable
        return {"type": "Yang", "is_changing": False, "binary": 1, "symbol": "---------"}
    elif value == 8: # Yin estable
        return {"type": "Yin", "is_changing": False, "binary": 0, "symbol": "---   ---"}
    else: # 9, Yang mutable
        return {"type": "Yang", "is_changing": True, "binary": 1, "symbol": "--- O ---"}

def generate_hexagram():
    """Genera las 6 líneas de un hexagrama, de abajo hacia arriba."""
    while True:
        lines = [get_line_properties(throw_coins()) for _ in range(6)]
        primary_binary = tuple(line["binary"] for line in lines)

        # Asegurarse de que el hexagrama generado es válido antes de continuar
        if primary_binary in HEXAGRAMS_BY_BINARY:
            # Si hay líneas mutables, calcula el hexagrama resultante
            has_changing_lines = any(line["is_changing"] for line in lines)
            resulting_binary = None
            if has_changing_lines:
                resulting_binary = tuple(1 - line["binary"] if line["is_changing"] else line["binary"] for line in lines)
                # No es necesario validar el resultante, ya que cualquier combinación de 6 líneas es un hexagrama válido.

            return lines, primary_binary, resulting_binary


def get_hexagram_info(binary_key):
    """Obtiene la información de un hexagrama a partir de su clave binaria."""
    return HEXAGRAMS_BY_BINARY.get(binary_key)

# --- Funciones de Visualización ---

def draw_hexagram(lines, title):
    """Dibuja un hexagrama usando Matplotlib."""
    fig, ax = plt.subplots(figsize=(2, 4))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.5, 5.5)
    ax.axis('off')
    ax.set_title(title, color='#c4a748', fontsize=14, pad=10)

    for i, line in enumerate(lines):
        color = '#c4a748' if line["is_changing"] else '#e6e6e6'
        ax.text(0.5, i, line["symbol"], fontsize=18, ha='center', va='center', color=color, fontfamily='monospace')
    
    return fig

# --- Interfaz de la Aplicación ---

# --- Barra Lateral (Sidebar) con Donaciones ---
st.sidebar.title("Support this Oracle")
st.sidebar.markdown("""
If you find value and wisdom in this tool, please consider a donation to support its maintenance and development. Your generosity is greatly appreciated.
""")

st.sidebar.markdown("---")

# --- Botón de Donación con PayPal ---
st.sidebar.header("Donate with PayPal")

paypal_button_html = """
<div class="centered-text">
    <a href="https://www.paypal.com/donate/?business=LND8CC9B5A8NA&no_recurring=0&item_name=Thank+you+for+supporting+the+Digital+I-Ching+Oracle.+Your+contribution+helps+keep+the+site+online.&currency_code=USD" target="_blank">
        <img src="https://www.paypalobjects.com/es_ES/i/btn/btn_donateCC_LG.gif" alt="Donar con PayPal">
    </a>
</div>
"""
# Nota: He generado un enlace de donación de PayPal más robusto para ti. Si prefieres usar el email directo, puedes construir una URL, pero los botones oficiales son más seguros y confiables para los usuarios.

st.sidebar.markdown(paypal_button_html, unsafe_allow_html=True)

st.sidebar.markdown("---")

# --- Donaciones con Criptomonedas ---
st.sidebar.header("Donate with Crypto")

btc_address = "154P7GdFHBH2N5XuSauBhEbdGYSen8RkBT"
doge_address = "DFT2oi1gsWFKiqqDhPabTud9NN6M2EbzhY"

st.sidebar.markdown(f'<p class="centered-text"><b>Bitcoin (BTC)</b></p>', unsafe_allow_html=True)
qr_code_html = f'<img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={btc_address}" class="qr-code" alt="BTC QR Code">'
st.sidebar.markdown(qr_code_html, unsafe_allow_html=True)
st.sidebar.markdown(f'<p class="centered-text" style="font-size: 12px; word-wrap: break-word;">{btc_address}</p>', unsafe_allow_html=True)

st.sidebar.markdown(f'<p class="centered-text" style="margin-top: 20px;"><b>Dogecoin (DOGE)</b></p>', unsafe_allow_html=True)
st.sidebar.markdown(f'<p class="centered-text" style="font-size: 12px; word-wrap: break-word;">{doge_address}</p>', unsafe_allow_html=True)

st.sidebar.markdown("---")

# --- Comunidad y Creador ---
st.sidebar.header("Community & Creator")
st.sidebar.markdown("""
Software developed by **Cha0smagick the technomage** for the chaos magic blog: **Practical Chaos Magic**.
""")
st.sidebar.markdown("[Blog: Practical Chaos Magic](https://grimoriomagiadelcaos.blogspot.com/)", unsafe_allow_html=True)
st.sidebar.markdown("[Telegram Channel](https://t.me/magiacaotica)", unsafe_allow_html=True)
st.sidebar.markdown("[Telegram Group](https://t.me/magiacaoticacoven)", unsafe_allow_html=True)


st.title("☯️ I-Ching Oracle")
st.markdown("### Reflect, ask, and find the wisdom of change.")

st.markdown("""
Welcome to the Digital Oracle. The I-Ching, or 'Book of Changes', is an ancient text that offers wisdom through the interpretation of hexagrams.

Take a moment to center your mind on a question or situation for which you seek clarity. It can be about your past, present, or future.
""")

question = st.text_area(
    "Enter your question here:",
    height=100,
    placeholder="e.g., What is the best attitude to take regarding my new project?"
)

if st.button("Consult the Oracle"):
    if not question.strip():
        st.warning("Please enter a question for the oracle to guide you.")
    else:
        with st.spinner("Casting the coins and consulting the sacred texts..."):
            time.sleep(random.uniform(1.5, 3)) # Simula la deliberación
            
            lines, primary_binary, resulting_binary = generate_hexagram()
            primary_hexagram = get_hexagram_info(primary_binary)
            resulting_hexagram = get_hexagram_info(resulting_binary) if resulting_binary else None

        st.success("The consultation is complete! This is the wisdom of the I-Ching for you.")
        st.markdown("---")
        
        st.markdown(f"#### For your question: *'{question.strip()}'*")
        st.markdown("---")

        # --- Mostrar Hexagramas ---
        col1, col2 = st.columns(2)
        with col1:
            fig_primary = draw_hexagram(lines, "Primary Hexagram")
            st.pyplot(fig_primary)
        
        if resulting_hexagram:
            with col2:
                # Crear líneas para el hexagrama resultante (invertir las mutables)
                resulting_lines_symbols = [
                    get_line_properties(throw_coins())['symbol'].replace('X', ' ').replace('O', ' ') # Placeholder
                    for i in range(6)
                ]
                resulting_lines_for_drawing = []
                for i, line in enumerate(lines):
                    new_binary = 1 - line["binary"] if line["is_changing"] else line["binary"]
                    symbol = "---   ---" if new_binary == 0 else "---------"
                    resulting_lines_for_drawing.append({"symbol": symbol, "is_changing": False})

                fig_resulting = draw_hexagram(resulting_lines_for_drawing, "Resulting Hexagram")
                st.pyplot(fig_resulting)

        # --- Interpretación del Hexagrama Primario ---
        st.header(f"Your Current Situation: ({primary_hexagram['num']}) {primary_hexagram['name_en']}")
        st.markdown(f"In response to your question, the oracle reveals the hexagram **{primary_hexagram['name_en']}**. This is a reflection of the energies surrounding you at this moment.")
        
        st.subheader("Oracle's Counsel")
        st.info(f"For your current situation, the oracle offers this central advice:")
        st.markdown(f"> {primary_hexagram['judgement']}")

        st.subheader("Attitude to Adopt")
        st.info(f"The wisdom of nature suggests you adopt the following attitude, inspired by the image of **{primary_hexagram['name_en']}**:")
        st.markdown(f"> {primary_hexagram['image']}")

        # --- Interpretación de Líneas Mutables ---
        changing_lines_info = [(i + 1, line) for i, line in enumerate(lines) if line["is_changing"]]
        if changing_lines_info:
            st.markdown("---")
            with st.expander("✨ The Heart of Change: Analysis of Changing Lines"):
                st.markdown("Your consultation has revealed moving lines. These are the most important dynamic forces in your situation—the points of tension and opportunity driving the transformation. Pay special attention to their messages, as they are the bridge between your present and your future.")
                for i, line in changing_lines_info:
                    line_texts = primary_hexagram.get("lines", [])
                    if len(line_texts) >= i:
                        line_text = line_texts[i-1]
                    else:
                        line_text = "Line text not found. Ensure data.py is complete."
                    st.markdown(f"#### Line {i} (changing {line['type']})")
                    st.warning(f"**Message:** {line_text}")
                    st.markdown(f"This line indicates that the `{line['type']}` energy at this position has reached a turning point and is transforming into its opposite, guiding the situation toward a new state.")

        # --- Interpretación del Hexagrama Resultante ---
        if resulting_hexagram:
            st.markdown("---")
            st.header(f"Where You Are Headed: ({resulting_hexagram['num']}) {resulting_hexagram['name_en']}")
            st.markdown(f"As a result of the change indicated by the moving lines, your situation is tending to evolve toward the hexagram **{resulting_hexagram['name_en']}**. This is the future landscape that is forming.")
            
            st.subheader("Counsel for the Future")
            st.markdown(f"> {resulting_hexagram['judgement']}")

            st.subheader("Attitude in the New Stage")
            st.markdown(f"> {resulting_hexagram['image']}")

st.markdown("---")
st.markdown("#### Final Reflection")
st.info("The oracle does not dictate an unchangeable future but offers you a mirror of the present energies. Use this wisdom to reflect, make more conscious decisions, and navigate the constant flow of change with greater clarity and confidence.")
