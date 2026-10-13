Leer en inglés: [README.md](./README.md)

![Elián Nahuel](https://img.shields.io/badge/Eli%C3%A1n%20Nahuel-Backend%20%7C%20Full--Stack%20Developer-blue?style=flat-square&logo=github)

<!-- Badges de tecnologías -->
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) ![SQLModel](https://img.shields.io/badge/SQLModel-009688?logo=pydantic&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-31648C?logo=sqlalchemy&logoColor=white) ![Alembic](https://img.shields.io/badge/Alembic-333333?logo=database&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?logo=postgresql&logoColor=white) ![DuckDB](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=black) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white) ![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white) ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)

# Backend Developer | Full-Stack Developer

Desarrollador Backend y Full-Stack de Argentina. **Técnico Superior en Desarrollo de Software** y estudiante de la **Licenciatura en Ciencia de Datos** en la **Universidad de la Ciudad de Buenos Aires (UDECI)**.

Especializado en APIs backend escalables, patrones de arquitectura resilientes, modelado de datos relacionales, orquestación de LLMs multi-proveedor y procesamiento analítico de alto rendimiento en el cliente.

---

## 🛠️ Enfoque Técnico y Capacidades

- **Backend y Modelado de Datos:** APIs REST asíncronas de alto rendimiento con FastAPI y Python 3.12; esquemas relacionales estrictos, migraciones y restricciones de integridad con PostgreSQL, SQLModel/SQLAlchemy y Alembic.
- **Ingeniería Arquitectónica:** Arquitecturas de dominio desacopladas (Hexagonal, Event-Driven, Transactional Outbox), estricta idempotencia y estrategias de replicación de datos offline-first.
- **Herramientas de IA y Orquestación LLM:** Integración multi-proveedor (Vercel AI SDK, Gemini, OpenAI, Groq), flujos conversacionales por streaming, auditorías automatizadas de repositorios y CVs, y salidas estructuradas deterministas.
- **Procesamiento de Datos en el Cliente:** Motores de consulta analítica en navegador mediante DuckDB-Wasm y WebAssembly para exploración de datos con latencia cero de servidor.

---

## 🚀 Proyectos Destacados

### [SkillRadar](https://github.com/eliann313/SkillRadar) — Plataforma Bilateral de Talento Impulsada por IA
- **Rol:** Creador y Desarrollador Principal
- **Descripción:** Plataforma bilateral de talento y reclutamiento impulsada por IA diseñada para revolucionar la contratación técnica mediante auditorías objetivas de cualificación.
- **Características Clave:** Puntuación ATS aditiva de base cero, auditorías profundas de repositorios de GitHub, simulador interactivo de entrevistas técnicas (voz/texto), Career Copilot y sanitización de datos personales con anonimización doble ciego (máscara de tokenización `DEV-XXXXXX` con cifrado AES-256-GCM).
- **Stack Tecnológico:** Next.js 16, React 19, TypeScript, Prisma, Neon Postgres, Vercel AI SDK (Gemini / OpenAI / Groq), Tailwind CSS.
- **Enlaces:** [Repositorio](https://github.com/eliann313/SkillRadar) | [Aplicación en Vivo](https://skillradar-app.vercel.app/)

### GridHub WMS (Enterprise / MVP Privado)
- **Rol:** Desarrollador Backend y Full-Stack
- **Descripción:** MVP comercial de gestión de depósitos y logística (WMS) diseñado para operaciones de inventario físico de alta concurrencia.
- **Ingeniería Enterprise:** Topología de almacenamiento estructurada en 7 zonas, restricciones de unicidad cuádruple (*quad-tuple constraints*) para prevenir stock fantasma, reglas de reabastecimiento automático, patrón Transactional Outbox para despacho desacoplado al ERP y sincronización offline-first en clientes móviles con IndexedDB (Dexie.js).
- **Stack Tecnológico:** Python 3.12, FastAPI, SQLModel, PostgreSQL, Alembic, React 19, TypeScript, Dexie.js, Vite PWA.
- > [!NOTE]
  > *GridHub WMS es un desarrollo comercial propietario alojado en un repositorio privado de organización. Aunque su código fuente y commits permanecen bajo confidencialidad comercial, su arquitectura productiva refleja altos estándares de consistencia transaccional y diseño backend distribuido.*

### [DataForge](https://github.com/eliann313/DataForge) — Plataforma de Analítica y Exploración de Datos Nativa del Navegador
- **Rol:** Creador y Desarrollador Principal
- **Descripción:** Plataforma analítica serverless que ejecuta consultas analíticas OLAP de forma local directamente en el navegador, sin necesidad de transferir datasets a servidores externos.
- **Características Clave:** Motor de consultas analíticas en memoria mediante DuckDB-Wasm, pipelines locales de transformación de datos, exploración interactiva de archivos Parquet/CSV y tiempos de respuesta de sub-milisegundos.
- **Stack Tecnológico:** DuckDB-Wasm, WebAssembly, TypeScript, React 19, Python, Tailwind CSS.
- **Enlaces:** [Repositorio](https://github.com/eliann313/DataForge)

### [Prop²](https://github.com/eliann313/Prop2) — Plataforma Inmobiliaria de Alto Rendimiento
- **Rol:** Desarrollador Full-Stack
- **Descripción:** Aplicación inmobiliaria moderna adaptada al mercado argentino construida bajo arquitectura modular limpia.
- **Características Clave:** Arquitectura hexagonal en Next.js, búsqueda full-text optimizada con PostgreSQL `tsvector`/GIN sincronizada con `searchParams` en la URL, subidas directas firmadas a Cloudinary, autenticación con Auth.js v5 y panel de gestión de listings y leads para vendedores.
- **Stack Tecnológico:** Next.js 16, TypeScript, React 19, PostgreSQL, Auth.js v5, Tailwind CSS, Cloudinary.
- **Enlaces:** [Repositorio](https://github.com/eliann313/Prop2)

### [Portfolio Personal](https://github.com/eliann313/mi-portfolio) — Showcase Técnico Interactivo
- **Rol:** Creador y Desarrollador Principal
- **Descripción:** Portfolio personal interactivo que documenta y visualiza decisiones de diseño, compensaciones arquitectónicas (*trade-offs*) y herramientas técnicas visuales.
- **Características Clave:** Diagramas de arquitectura C4 interactivos, explorador relacional e inspector de canvas ERD con panel deslizable (*slide-over drawer*) de cero scroll, bitácoras de decisiones arquitectónicas y soporte bilingüe (i18n).
- **Stack Tecnológico:** React 19, TypeScript, Vite, Tailwind CSS, Framer Motion.
- **Enlaces:** [Repositorio](https://github.com/eliann313/mi-portfolio) | [Portfolio en Vivo](https://elian-nahuel-portfolio.vercel.app/)

---

### Proyectos Colaborativos y Académicos

- **[Pochocleando](https://github.com/Antonio-sharp-plus/Pochocleando)**: Plataforma colaborativa de descubrimiento y reseñas de cine.  
  *Stack:* Angular, Express, Node.js, MongoDB.
- **[PokeApp](https://github.com/bunicodea/proyecto-pokedex)**: Aplicación móvil/web didáctica de Pokédex.  
  *Stack:* Ionic, Angular, Firebase.

---

## 📊 Estadísticas de GitHub y Badges Rápidos

- ![Seguidores](./assets/badges/followers.svg)
- ![Repositorios públicos](./assets/badges/public-repos.svg)

| Proyecto | Lenguaje Principal | Última Actividad |
|:---|:---:|:---:|
| **SkillRadar** | ![Lenguaje principal](./assets/badges/eliann313-SkillRadar-lang.svg) | ![Último commit](./assets/badges/eliann313-SkillRadar-commit.svg) |
| **GridHub WMS** | ![Lenguaje principal](./assets/badges/Juamp1Sch-WMS-lang.svg) | ![Último commit](./assets/badges/Juamp1Sch-WMS-commit.svg) |
| **DataForge** | ![Lenguaje principal](./assets/badges/eliann313-DataForge-lang.svg) | ![Último commit](./assets/badges/eliann313-DataForge-commit.svg) |
| **Prop²** | ![Lenguaje principal](./assets/badges/eliann313-Prop2-lang.svg) | ![Último commit](./assets/badges/eliann313-Prop2-commit.svg) |
| **Portfolio Personal** | ![Lenguaje principal](./assets/badges/eliann313-mi-portfolio-lang.svg) | ![Último commit](./assets/badges/eliann313-mi-portfolio-commit.svg) |
| **Pochocleando** | ![Lenguaje principal](./assets/badges/Antonio-sharp-plus-Pochocleando-lang.svg) | ![Último commit](./assets/badges/Antonio-sharp-plus-Pochocleando-commit.svg) |
| **PokeApp** | ![Lenguaje principal](./assets/badges/bunicodea-proyecto-pokedex-lang.svg) | ![Último commit](./assets/badges/bunicodea-proyecto-pokedex-commit.svg) |

---

## 📬 Contacto

- 🌐 **Portfolio:** [elian-nahuel-portfolio.vercel.app](https://elian-nahuel-portfolio.vercel.app/)
- 💼 **LinkedIn:** [linkedin.com/in/eliannahuel](https://www.linkedin.com/in/eliannahuel)
- 📧 **Email:** [elian.nahuel0348@gmail.com](mailto:elian.nahuel0348@gmail.com)

[![SkillRadar](https://skillradar-app.vercel.app/api/badge/eliann313)](https://skillradar-app.vercel.app/u/eliann313)
