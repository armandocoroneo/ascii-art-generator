# 🎨 ASCII Art Generator - Cloning

Convierte imágenes a arte ASCII y clónalas en múltiples patrones. Disponible en **web** (HTML puro) y **Streamlit**.

---

## 📋 Características

✅ **Conversión de imágenes a ASCII**
- Carga imágenes (JPG, PNG, GIF)
- Ajusta ancho y caracteres personalizados
- Invierte colores/brillo

✅ **Clonado automático**
- 2x1, 4x1 Horizontal
- 2x1, 4x1 Vertical
- Grillas 2x2 y 4x4

✅ **Diseños preestablecidos**
- Cuadrado, Árbol, Corazón, Diamante, Onda, Estrella

✅ **Descarga múltiple**
- .BBCODE (optimizado para foros)
- .TXT (texto plano)
- Copiar al portapapeles

✅ **Compartir por enlace**
- Comparte ASCII codificado en URL
- Sin servidor (todo en el navegador)

✅ **Tema claro/oscuro**
- Toggle manual
- Persiste en localStorage

---

## 🚀 Uso Rápido

### Opción 1: Web (HTML puro)

```bash
# Abrir directamente en navegador
web/index.html

# O en Windows, doble clic en:
web/run.bat
```

**Ventajas:**
- ✨ Funcionamiento 100% offline
- ⚡ Sin dependencias
- 🔒 Privacidad total (nada se guarda)

---

### Opción 2: Streamlit (en línea)

#### Local:
```bash
cd streamlit
pip install -r requirements.txt
streamlit run app.py
```

#### En Streamlit Cloud (gratis):
1. Fork este repo a tu GitHub
2. Ve a [streamlit.io/cloud](https://streamlit.io/cloud)
3. Conecta el repo
4. Deploy automático ✨

**Ventajas:**
- 🌐 Acceso desde cualquier lugar
- 👥 Compartible por URL
- 🎨 Interfaz mejorada

---

## 📂 Estructura

```
ascii-art-generator-repo/
├── web/
│   ├── index.html          # App web (standalone)
│   └── run.bat             # Launcher para Windows
├── streamlit/
│   ├── app.py              # App Streamlit
│   └── requirements.txt     # Dependencias Python
├── README.md               # Este archivo
└── .gitignore
```

---

## 🎯 Ejemplos

### Conversión de imagen a ASCII
```
Imagen PNG (100x100px)
         ↓
Selecciona ancho (ej: 100 caracteres)
         ↓
Elige charset (Bloques, Gradiente, Símbolos)
         ↓
🎨 ASCII generado
```

### Clonado
```
Original:   Clonado 2x1 Horizontal:
  ◆          ◆  ◆
◆ ◆        ◆ ◆  ◆ ◆
  ◆          ◆  ◆
```

### Descarga
```
ASCII → .BBCODE → [code] ... [/code]
     → .TXT
     → Portapapeles
```

---

## 🔐 Privacidad

- **Web**: 100% cliente (navegador)
- **Streamlit**: Imagen procesada, no guardada
- **Compartir**: URL sin servidor (base64 en URL)

---

## 🛠️ Instalación Local (Streamlit)

### Requisitos
- Python 3.8+
- pip

### Pasos
```bash
# Clonar repo
git clone https://github.com/armandocoroneo/ascii-art-generator.git
cd ascii-art-generator/streamlit

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app.py
```

Se abre automáticamente en `http://localhost:8501`

---

## 📦 Desplegando en Streamlit Cloud

1. **Fork este repo** en GitHub
2. **Conecta Streamlit Cloud**
   - Ve a [streamlit.io/cloud](https://streamlit.io/cloud)
   - Inicia sesión con GitHub
   - Elige este repo
3. **Selecciona carpeta principal**: `streamlit/`
4. **Deploy**: ¡Listo! 🎉

### URL de ejemplo
```
https://share.streamlit.io/[tu-usuario]/ascii-art-generator/streamlit/app.py
```

---

## 🤝 Contribuir

1. Fork el repo
2. Crea una rama: `git checkout -b feature/mejora`
3. Commit: `git commit -am 'Agrega mejora'`
4. Push: `git push origin feature/mejora`
5. Pull Request

---

## 📝 Licencia

MIT License - Libre para uso personal y comercial

---

## 👤 Autor

**armandocoroneo**  
GitHub: [@armandocoroneo](https://github.com/armandocoroneo)

---

## 💡 Roadmap (TODOs)

- [ ] API REST para terceros
- [ ] Más charsets personalizados
- [ ] Animaciones ASCII
- [ ] Soporte para video/GIF
- [ ] Historial de conversiones
- [ ] Exportar como imagen PNG

---

## 🐛 Reportar bugs

Issues en GitHub: [Issues](https://github.com/armandocoroneo/ascii-art-generator/issues)

---

**Versión:** 1.0.0  
**Última actualización:** 2026-10-17

