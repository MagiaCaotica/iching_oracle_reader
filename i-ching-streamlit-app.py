# -*- coding: utf-8 -*-
import streamlit as st
import random
import matplotlib.pyplot as plt
import time
from data import HEXAGRAM_DATA

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Oráculo I-Ching Digital",
    page_icon="☯️",
    layout="centered",
    initial_sidebar_state="collapsed",
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
</style>
""", unsafe_allow_html=True)

# --- Lógica del I-Ching ---

@st.cache_data
def load_hexagram_data():
    """Carga y mapea los datos de los hexagramas para una búsqueda rápida."""
    return {h["binary"]: h for h in HEXAGRAM_DATA}

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

st.title("☯️ Oráculo del I-Ching")
st.markdown("### Reflexiona, pregunta y encuentra la sabiduría del cambio.")

st.markdown("""
Bienvenido al Oráculo Digital. El I-Ching, o 'Libro de los Cambios', es un texto milenario que ofrece sabiduría a través de la interpretación de hexagramas.

Tómate un momento para centrar tu mente en una pregunta o situación sobre la que buscas claridad. Puede ser sobre tu pasado, presente o futuro.
""")

question = st.text_area(
    "Escribe aquí tu pregunta:",
    height=100,
    placeholder="Ej: ¿Cuál es la mejor actitud a tomar respecto a mi nuevo proyecto?"
)

if st.button("Consultar al Oráculo"):
    if not question.strip():
        st.warning("Por favor, escribe una pregunta para que el oráculo pueda guiarte.")
    else:
        with st.spinner("Lanzando las monedas y consultando los textos sagrados..."):
            time.sleep(random.uniform(1.5, 3)) # Simula la deliberación
            
            lines, primary_binary, resulting_binary = generate_hexagram()
            primary_hexagram = get_hexagram_info(primary_binary)
            resulting_hexagram = get_hexagram_info(resulting_binary) if resulting_binary else None

        st.success("¡La consulta ha finalizado! Esta es la sabiduría del I-Ching para ti.")
        st.markdown("---")

        # --- Mostrar Hexagramas ---
        col1, col2 = st.columns(2)
        with col1:
            fig_primary = draw_hexagram(lines, "Hexagrama Primario")
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

                fig_resulting = draw_hexagram(resulting_lines_for_drawing, "Hexagrama Resultante")
                st.pyplot(fig_resulting)

        # --- Interpretación del Hexagrama Primario ---
        st.header(f"({primary_hexagram['num']}) {primary_hexagram['name_es']} - {primary_hexagram['name_ch']}")
        
        st.subheader("El Juicio")
        st.markdown(f"> {primary_hexagram['judgement']}")

        st.subheader("La Imagen")
        st.markdown(f"> {primary_hexagram['image']}")

        # --- Interpretación de Líneas Mutables ---
        changing_lines_info = [(i + 1, line) for i, line in enumerate(lines) if line["is_changing"]]
        if changing_lines_info:
            with st.expander("✨ Análisis de las Líneas Mutables"):
                st.markdown("Las líneas mutables indican las fuerzas dinámicas en tu situación. Presta especial atención a sus mensajes, ya que revelan el camino hacia el hexagrama resultante.")
                for i, line in changing_lines_info:
                    st.markdown(f"**Línea {i} ({line['type']} mutable):** Tu situación contiene una energía de cambio que se transforma en su opuesto.")

        # --- Interpretación del Hexagrama Resultante ---
        if resulting_hexagram:
            st.markdown("---")
            st.header(f"Tendencia: ({resulting_hexagram['num']}) {resulting_hexagram['name_es']} - {resulting_hexagram['name_ch']}")
            st.markdown("Este hexagrama muestra la dirección hacia la que evoluciona tu situación actual.")
            
            st.subheader("El Juicio")
            st.markdown(f"> {resulting_hexagram['judgement']}")

            st.subheader("La Imagen")
            st.markdown(f"> {resulting_hexagram['image']}")

st.markdown("---")
st.info("Recuerda: el oráculo no predice el futuro, sino que ofrece una perspectiva para ayudarte a tomar decisiones más conscientes y alineadas con el fluir del universo.")
