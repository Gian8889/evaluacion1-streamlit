import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as funcs
import libreria_clases_proyecto1 as clases

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="Proyecto 1 - Python Fundamentals", page_icon="🚀", layout="centered")

# ==========================================
# MEMORIA DE LA APP (st.session_state)
# Evita que los datos se borren al hacer clic en botones
# ==========================================
if "movimientos_ej1" not in st.session_state:
    st.session_state.movimientos_ej1 = []  # Lista para Ejercicio 1

if "productos_ej2" not in st.session_state:
    # Diccionario de arrays NumPy para Ejercicio 2
    st.session_state.productos_ej2 = {
        "Nombre": np.array([], dtype=str),
        "Categoría": np.array([], dtype=str),
        "Precio": np.array([], dtype=float),
        "Cantidad": np.array([], dtype=int),
        "Total": np.array([], dtype=float)
    }

if "historico_ej3" not in st.session_state:
    st.session_state.historico_ej3 = []  # Lista para histórico del Ejercicio 3


if "crud_inventario_ej4" not in st.session_state:
    st.session_state.crud_inventario_ej4 = {}  # Diccionario vacío para el CRUD de Empleados

# ==========================================
# MENÚ LATERAL (Obligatorio)
# ==========================================
st.sidebar.title("🧭 Menú de Navegación")
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# 1. SECCIÓN HOME
# ==========================================
if opcion == "Home":
    st.title("🚀 Proyecto 1 - Aplicación Interactiva")
    st.subheader("Especialización en Python potenciada por IA")
    st.markdown("**Módulo 1:** Python Fundamentals")
    
    st.markdown("---")
    
    # Imagen / Logo representativo (Usa una URL pública o súbela a tu GitHub)
    st.image("https://www.python.org/static/community_logos/python-logo-master-v3-TM.png", width=250)
    
    # Información del estudiante (Rellena con tus datos reales)
    st.markdown("### 👤 Información del Estudiante")
    st.write("**Nombre Completo:** Jorge Giancarlo Huaman Calderon")
    st.write("**Instructor:** MSc. Carlos Carrillo Villavicencio")
    st.write("**Año:** 2026")
    
    st.markdown("### 📝 Descripción del Proyecto")
    st.write("""
    Esta aplicación interactiva consolida los fundamentos de programación en Python analizados en clase.
    A través de las secciones, se evidencia el control de flujos con estructuras de datos (listas y arrays), 
    la creación de dataframes interactivos, manipulación de funciones modulares y programación orientada a objetos (CRUD).
    """)
    
    st.markdown("### 🛠️ Tecnologías Utilizadas")
    st.markdown("- **Python 3**\n- **Streamlit** (Interfaz de usuario)\n- **NumPy** (Vectores y cálculo estructurado)\n- **Pandas** (Estructuras de datos en tablas / DataFrames)")

# ==========================================
# 2. EJERCICIO 1: Flujo de Caja con Listas
# ==========================================
elif opcion == "Ejercicio 1":
    st.title("💸 Ejercicio 1: Flujo de Caja con Listas")
    st.markdown("""
    *Descripción:* Módulo dinámico para registrar movimientos financieros dentro de una lista vacía en memoria. 
    Permite calcular totales de ingresos, gastos, saldo final y determinar el estado del flujo de caja.
    """)
    
    st.markdown("### 📝 Ingresar Movimiento")
    
    # Widgets de captura
    concepto = st.text_input("Concepto / Descripción:", placeholder="Ej. Pago de membresía, Venta de producto")
    tipo_movimiento = st.selectbox("Tipo de Movimiento:", ["Ingreso", "Gasto"])
    valor = st.number_input("Monto ($):", min_value=0.0, step=10.0, format="%.2f")
    
    # Botón para añadir a la lista
    if st.button("Agregar Movimiento", key="btn_ej1"):
        if concepto.strip() == "":
            st.warning("⚠️ Por favor, ingresa un concepto válido.")
        elif valor <= 0:
            st.warning("⚠️ El monto debe ser mayor a 0.")
        else:
            # Creamos un diccionario para el movimiento actual
            nuevo_movimiento = {
                "Concepto": concepto,
                "Tipo": tipo_movimiento,
                "Valor": valor
            }
            # Agregamos a la lista guardada en la sesión
            st.session_state.movimientos_ej1.append(nuevo_movimiento)
            st.success(f"✅ ¡Movimiento '{concepto}' registrado con éxito!")

    st.markdown("---")
    st.markdown("### 📊 Historial y Balance Final")
    
    if len(st.session_state.movimientos_ej1) > 0:
        # Convertimos la lista de diccionarios en un DataFrame para mostrarlo como tabla ordenada
        df_movimientos = pd.DataFrame(st.session_state.movimientos_ej1)
        st.dataframe(df_movimientos, use_container_width=True)
        
        # Operaciones y cálculos sobre la lista
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos_ej1 if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos_ej1 if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos
        
        # Mostrar métricas visuales atractivas
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"${total_ingresos:,.2f}")
        col2.metric("Total Gastos", f"${total_gastos:,.2f}")
        col3.metric("Saldo Final", f"${saldo_final:,.2f}")
        
        # Alertas de estado del Flujo de caja
        if saldo_final >= 0:
            st.success(f"📈 El flujo de caja está **A FAVOR** por un monto de ${saldo_final:,.2f}")
        else:
            st.error(f"📉 El flujo de caja está **EN CONTRA** por un monto de ${abs(saldo_final):,.2f}")
    else:
        st.info("ℹ️ No hay movimientos registrados todavía. Usa el formulario de arriba.")

# ==========================================
# 3. EJERCICIO 2: Registro con NumPy Arrays
# ==========================================
elif opcion == "Ejercicio 2":
    st.title("📊 Ejercicio 2: Registro con NumPy y DataFrames")
    st.markdown("""
    *Descripción:* Formulario de inventario que recopila registros, los almacena utilizando estructuras vectoriales de **NumPy Arrays** y los concatena dinámicamente en un objeto DataFrame.
    """)
    
    st.markdown("### 🛒 Formulario de Productos")
    
    col_a, col_b = st.columns(2)
    with col_a:
        prod_nombre = st.text_input("Nombre del Producto:", key="prod_nom")
        prod_categoria = st.selectbox("Categoría:", ["Electrónica", "Alimentos", "Ropa", "Hogar", "Otros"])
    with col_b:
        prod_precio = st.number_input("Precio Unitario ($):", min_value=0.0, step=1.0, format="%.2f")
        prod_cantidad = st.number_input("Cantidad Disponible:", min_value=1, step=1)
    
    prod_total = prod_precio * prod_cantidad
    st.write(f"**Total Calculado:** ${prod_total:,.2f}")
    
    if st.button("Agregar a Inventario", key="btn_ej2"):
        if prod_nombre.strip() == "":
            st.warning("⚠️ Digita un nombre válido para el producto.")
        else:
            # Extraemos los arreglos actuales desde la sesión
            arr_nom = st.session_state.productos_ej2["Nombre"]
            arr_cat = st.session_state.productos_ej2["Categoría"]
            arr_pre = st.session_state.productos_ej2["Precio"]
            arr_cant = st.session_state.productos_ej2["Cantidad"]
            arr_tot = st.session_state.productos_ej2["Total"]
            
            # Usamos np.append() para añadir los nuevos elementos simulando la estructura NumPy
            st.session_state.productos_ej2["Nombre"] = np.append(arr_nom, prod_nombre)
            st.session_state.productos_ej2["Categoría"] = np.append(arr_cat, prod_categoria)
            st.session_state.productos_ej2["Precio"] = np.append(arr_pre, prod_precio)
            st.session_state.productos_ej2["Cantidad"] = np.append(arr_cant, prod_cantidad)
            st.session_state.productos_ej2["Total"] = np.append(arr_tot, prod_total)
            
            st.success(f"📦 Producto '{prod_nombre}' agregado a los arreglos de NumPy.")

    st.markdown("---")
    st.markdown("### 📋 Inventario Actualizado (DataFrame)")
    
    # Convertimos el diccionario de NumPy arrays a un DataFrame visible
    df_inventario = pd.DataFrame(st.session_state.productos_ej2)
    
    if not df_inventario.empty:
        st.dataframe(df_inventario, use_container_width=True)
        # Información estadística rápida con funciones NumPy
        total_invertido = np.sum(st.session_state.productos_ej2["Total"])
        st.info(f"💰 **Valor Total del Inventario acumulado:** ${total_invertido:,.2f}")
    else:
        st.info("ℹ️ El inventario está vacío.")

# ==========================================
# 4. EJERCICIO 3: Librería de Funciones
# ==========================================
# ==========================================
# 4. EJERCICIO 3: Uso de Funciones desde Librería Externa
# ==========================================
elif opcion == "Ejercicio 3":
    st.title("📈 Ejercicio 3: Uso de Funciones desde Librería Externa")
    st.markdown("""
    *Descripción:* Módulo que conecta funciones de negocio alojadas en un módulo independiente (`libreria_funciones_proyecto1.py`).
    Permite evaluar el comportamiento financiero mediante cálculos interactivos de Punto de Equilibrio y registrar el histórico de simulaciones.
    """)

    # 1. Selector de Función (Requisito Obligatorio)
    st.markdown("### 🔍 Selector de Función")
    funcion_seleccionada = st.selectbox(
        "Selecciona una función de acuerdo a tu área de formación:",
        ["calcular_punto_equilibrio (Análisis de Costos y Finanzas)"]
    )

    st.markdown("---")
    st.markdown("### 📥 Parámetros de la Función")

    # 2. Widgets para ingresar parámetros en columnas ordenadas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        costos_fijos = st.number_input(
            "Costos Fijos Totales ($):", 
            min_value=0.0, 
            value=1000.0, 
            step=100.0, 
            format="%.2f",
            help="Gastos constantes mensuales (Luz, Alquiler, Sueldos fijos)."
        )
    with col2:
        precio_unitario = st.number_input(
            "Precio Unitario ($):", 
            min_value=0.01, 
            value=50.0, 
            step=5.0, 
            format="%.2f",
            help="Precio de venta al público de una sola unidad o servicio (ej. Entrada de sauna)."
        )
    with col3:
        costo_variable_unitario = st.number_input(
            "Costo Variable Unitario ($):", 
            min_value=0.0, 
            value=20.0, 
            step=5.0, 
            format="%.2f",
            help="Costo asociado directamente a la producción de una unidad (ej. Lavado de toallas, esencias)."
        )

    # 3. Botón para ejecutar la acción
    if st.button("Ejecutar Función Financiera", key="btn_ej3"):
        # Validación de negocio antes de llamar al script externo
        if precio_unitario <= costo_variable_unitario:
            st.error("❌ **Error crítico:** El Precio Unitario debe ser estrictamente mayor que el Costo Variable Unitario, de lo contrario el negocio jamás cubrirá sus costos.")
        else:
            try:
                # 🚀 LLAMADA A TU LIBRERÍA EXTERNA (Usando el alias 'funcs')
                resultado = funcs.calcular_punto_equilibrio(
                    costos_fijos=costos_fijos,
                    precio_unitario=precio_unitario,
                    costo_variable_unitario=costo_variable_unitario
                )

                # 4. Mostrar el resultado en pantalla de manera atractiva
                st.success("🎯 ¡Cálculo realizado con éxito!")
                
                res_col1, res_col2, res_col3 = st.columns(3)
                res_col1.metric("Margen de Contribución", f"${resultado['margen_contribucion_unitario']:,.2f}")
                res_col2.metric("Punto de Equilibrio (Unidades)", f"{resultado['punto_equilibrio_unidades']:,} und")
                res_col3.metric("Punto de Equilibrio (Ventas)", f"${resultado['punto_equilibrio_ventas']:,.2f}")

                # 5. Guardar en el histórico de resultados (Mochila del Session State)
                nuevo_registro = {
                    "Función": "Punto Equilibrio",
                    "Costos Fijos ($)": costos_fijos,
                    "Precio Unitario ($)": precio_unitario,
                    "Costo Var. Unitario ($)": costo_variable_unitario,
                    "Margen Contribución ($)": resultado['margen_contribucion_unitario'],
                    "PE Unidades": resultado['punto_equilibrio_unidades'],
                    "PE Ventas ($)": resultado['punto_equilibrio_ventas']
                }
                st.session_state.historico_ej3.append(nuevo_registro)

            except Exception as e:
                st.error(f"🚨 Error al ejecutar la librería externa: {e}")

    st.markdown("---")
    st.markdown("### 📋 Tabla Histórica de Resultados (DataFrame)")

    # 6. Mostrar tabla histórica recopilada
    if len(st.session_state.historico_ej3) > 0:
        df_historico = pd.DataFrame(st.session_state.historico_ej3)
        st.dataframe(df_historico, use_container_width=True)
        
        # Pequeño análisis extra de regalo con NumPy
        pe_promedio = np.mean(df_historico["PE Unidades"])
        st.light_trend = True # Indicador visual ficticio
        st.info(f"ℹ️ El punto de equilibrio promedio de todas las simulaciones guardadas es de **{pe_promedio:,.2f} unidades**.")
    else:
        st.info("ℹ️ No se han ejecutado simulaciones en esta sesión. Completa los campos y presiona el botón.")

# ==========================================
# 5. EJERCICIO 4: CRUD de Clases
# ==========================================
elif opcion == "Ejercicio 4":
    st.title("🧠 Ejercicio 4: Control de Clases con Sistema CRUD")
    st.write("Conecta aquí la clase elegida de tu archivo `librería_clases_proyecto1.py` para aplicar Crear, Leer, Actualizar y Eliminar.")
    
    # TODO: Aquí programaremos las pestañas (tabs) para hacer el Crear, Leer, Actualizar y Borrar.
