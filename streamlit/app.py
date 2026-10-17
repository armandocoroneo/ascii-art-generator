
import streamlit as st
from PIL import Image
import io
import base64
from datetime import datetime

st.set_page_config(
    page_title="ASCII Art Generator - Cloning",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .header-ascii {
        text-align: center;
        font-family: 'Courier New', monospace;
        font-size: 16px;
        line-height: 1.2;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .stats-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        margin: 15px 0;
    }
    .stat-box {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 5px;
        text-align: center;
    }
    .ascii-output {
        background-color: #f5f5f5;
        border: 1px solid #ddd;
        padding: 15px;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-size: 12px;
        line-height: 1.2;
        white-space: pre;
        overflow-x: auto;
        max-height: 500px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-ascii">
╔═══════════════════════════════════════╗<br>
║  ASCII ART GENERATOR - CLONING  ║<br>
╚═══════════════════════════════════════╝<br>
Convierte imágenes a ASCII y clónalas
</div>
""", unsafe_allow_html=True)

# Presets
PRESETS = {
    'Cuadrado': [
        "┌─────┐",
        "│ ╔═╗ │",
        "│ ║█║ │",
        "│ ╚═╝ │",
        "└─────┘"
    ],
    'Árbol': [
        "    △",
        "   ╱│╲",
        "  ╱ │ ╲",
        "   ┃┃┃",
        "   ┃┃┃"
    ],
    'Corazón': [
        " ♥♥ ♥♥",
        "♥   ♥",
        "♥   ♥",
        " ♥ ♥ ",
        "  ♥  "
    ],
    'Diamante': [
        "   ◆   ",
        "  ◆ ◆  ",
        " ◆   ◆ ",
        "  ◆ ◆  ",
        "   ◆   "
    ],
    'Onda': [
        "~~~∿~~~",
        "∿~~~∿~~",
        "~~~∿~~~",
        "∿~~~∿~~"
    ],
    'Estrella': [
        "   ★   ",
        "  ★ ★  ",
        "★ ★ ★ ★",
        "  ★ ★  ",
        "   ★   "
    ]
}

CHARSETS = {
    'Bloques: ░▒▓█': '░▒▓█',
    'Gradiente: @%#*+=-:.': '@%#*+=-:.',
    'Símbolos: ◆▲◇▼': '◆▲◇▼',
    'Mixto: @#%*+-=.': '@#%*+-=.'
}

CLONE_MODES = {
    '2x1 Horizontal': 'h2x1',
    '4x1 Horizontal': 'h4x1',
    '2x1 Vertical': 'v2x1',
    '4x1 Vertical': 'v4x1',
    'Grilla 2x2': 'grid2x2',
    'Grilla 4x4': 'grid4x4'
}

# Initialize session state
if 'current_ascii' not in st.session_state:
    st.session_state.current_ascii = ''
if 'current_image' not in st.session_state:
    st.session_state.current_image = None

# Sidebar
st.sidebar.markdown("## ⚙️ CONFIGURACIÓN")

input_method = st.sidebar.radio(
    "Selecciona entrada:",
    ("Cargar Imagen", "Diseño Preestablecido")
)

if input_method == "Cargar Imagen":
    uploaded_file = st.sidebar.file_uploader("Sube una imagen", type=['jpg', 'jpeg', 'png', 'gif'])
    if uploaded_file:
        st.session_state.current_image = Image.open(uploaded_file)
        st.sidebar.success(f"✓ {uploaded_file.name} ({st.session_state.current_image.width}x{st.session_state.current_image.height}px)")
else:
    preset = st.sidebar.selectbox("Elige un diseño", list(PRESETS.keys()))
    if st.sidebar.button("📌 Cargar Diseño", use_container_width=True):
        st.session_state.current_ascii = '\n'.join(PRESETS[preset])
        st.rerun()

st.sidebar.markdown("---")

width = st.sidebar.slider("Ancho ASCII (caracteres)", 20, 200, 100)
charset_name = st.sidebar.selectbox("Caracteres a usar", list(CHARSETS.keys()))
charset = CHARSETS[charset_name]
invert = st.sidebar.checkbox("Invertir colores")

st.sidebar.markdown("---")

if st.sidebar.button("🔄 CONVERTIR A ASCII", use_container_width=True, type="primary"):
    if st.session_state.current_image:
        with st.spinner("Convirtiendo imagen..."):
            img = st.session_state.current_image
            img_array = img.convert('RGB')
            pixels = img_array.load()
            
            height = round((img.height / img.width) * width * 0.55)
            img_resized = img.resize((width, height))
            
            ascii_art = ''
            img_pixels = img_resized.load()
            
            for y in range(height):
                for x in range(width):
                    r, g, b = img_pixels[x, y][:3]
                    brightness = (r + g + b) / 3
                    index = int((brightness / 255) * (len(charset) - 1))
                    if invert:
                        index = len(charset) - 1 - index
                    ascii_art += charset[index]
                ascii_art += '\n'
            
            st.session_state.current_ascii = ascii_art
            st.session_state.current_image = None
            st.success("✓ Conversión exitosa")
            st.rerun()
    else:
        st.error("Carga una imagen primero")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 INPUT")
    if st.session_state.current_image:
        st.image(st.session_state.current_image, use_column_width=True)

with col2:
    st.markdown("### 🎨 OUTPUT & CLONING")
    
    if st.session_state.current_ascii:
        st.markdown('<div class="ascii-output">' + st.session_state.current_ascii.replace('<', '&lt;').replace('>', '&gt;') + '</div>', unsafe_allow_html=True)
        
        lines = len(st.session_state.current_ascii.split('\n'))
        chars = len(st.session_state.current_ascii)
        size_kb = len(st.session_state.current_ascii.encode('utf-8')) / 1024
        
        col_l, col_c, col_s = st.columns(3)
        with col_l:
            st.metric("Líneas", lines)
        with col_c:
            st.metric("Caracteres", chars)
        with col_s:
            st.metric("Tamaño", f"{size_kb:.2f} KB")
    else:
        st.info("(ASCII aparecerá aquí)")

# Cloning options
st.markdown("### 🔀 OPCIONES DE CLONADO")

col1, col2, col3 = st.columns(3)

def clone_ascii(mode):
    if not st.session_state.current_ascii:
        st.error("No hay ASCII para clonar")
        return
    
    lines = st.session_state.current_ascii.split('\n')
    cloned = []
    
    if mode == 'h2x1':
        cloned = [line + '  ' + line for line in lines]
    elif mode == 'h4x1':
        cloned = [line + '  ' + line + '  ' + line + '  ' + line for line in lines]
    elif mode == 'v2x1':
        cloned = lines + [''] + lines
    elif mode == 'v4x1':
        cloned = lines + [''] + lines + [''] + lines + [''] + lines
    elif mode == 'grid2x2':
        cloned = [line + '  ' + line for line in lines]
        cloned.append('')
        cloned += [line + '  ' + line for line in lines]
    elif mode == 'grid4x4':
        for i in range(4):
            cloned += [line + '  ' + line + '  ' + line + '  ' + line for line in lines]
            if i < 3:
                cloned.append('')
    
    st.session_state.current_ascii = '\n'.join(cloned)
    st.success(f"✓ Clonado: {mode}")
    st.rerun()

with col1:
    if st.button("2x1 Horizontal", use_container_width=True):
        clone_ascii('h2x1')
    if st.button("2x1 Vertical", use_container_width=True):
        clone_ascii('v2x1')

with col2:
    if st.button("4x1 Horizontal", use_container_width=True):
        clone_ascii('h4x1')
    if st.button("4x1 Vertical", use_container_width=True):
        clone_ascii('v4x1')

with col3:
    if st.button("Grilla 2x2", use_container_width=True):
        clone_ascii('grid2x2')
    if st.button("Grilla 4x4", use_container_width=True):
        clone_ascii('grid4x4')

# Download options
st.markdown("### 💾 DESCARGAR")

col1, col2, col3 = st.columns(3)

with col1:
    if st.session_state.current_ascii:
        st.download_button(
            label="📋 Copiar a Portapapeles",
            data=st.session_state.current_ascii,
            file_name=f"ascii_art_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

with col2:
    if st.session_state.current_ascii:
        bbcode_content = f"[code]\n{st.session_state.current_ascii}\n[/code]"
        st.download_button(
            label="💾 Descargar .BBCODE",
            data=bbcode_content,
            file_name=f"ascii_art_{datetime.now().strftime('%Y%m%d_%H%M%S')}.bbcode",
            mime="text/plain",
            use_container_width=True
        )

with col3:
    if st.session_state.current_ascii:
        st.download_button(
            label="📄 Descargar .TXT",
            data=st.session_state.current_ascii,
            file_name=f"ascii_art_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

if st.button("🗑️ Limpiar Todo", use_container_width=True):
    st.session_state.current_ascii = ''
    st.session_state.current_image = None
    st.success("✓ Limpiado")
    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888;">
🔐 Todo se procesa en el servidor de Streamlit. | ⚡ Imágenes procesadas no se guardan.
</div>
""", unsafe_allow_html=True)
