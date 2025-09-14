from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from pathlib import Path

path = Path("index.html")

app = FastAPI()

# <a href="http://127.0.0.1:8000/ai"><h3>Искусственный Интеллект</h3></a>
#                 <p>Нейронные сети, машинное обучение и генеративный ИИ, способные создавать контент, анализировать данные и принимать решения.</p>
#             </div>
#             <div class="tech-card">
#                 <div class="tech-icon">
#                     <i class="fas fa-microchip"></i>
#                 </div>
#                 <a href="http://127.0.0.1:8000/quantum"><h3>Квантновые вычисления</h3></a>
#                 <p>Компьютеры, способные решать задачи, недоступные классическим суперкомпьютерам, за счет использования квантовых битов.</p>
#             </div>
#             <div class="tech-card">
#                 <div class="tech-icon">
#                     <i class="fas fa-dna"></i>
#                 </div>
#                 <a href="http://127.0.0.1:8000/genetics"><h3>Генная инженерия</h3></a>
#                 <p>CRISPR и другие технологии редактирования генома, позволяющие лечить наследственные заболевания и улучшать качества организмов.</p>
#             </div>
#             <div class="tech-card">
#                 <div class="tech-icon">
#                     <i class="fas fa-globe"></i>
#                 </div>
#                 <a href="http://127.0.0.1:8000/blockchain"><h3>Блокчейн</h3></a>
#                 <p>Децентрализованные системы, обеспечивающие прозрачность, безопасность и отсутствие посредников в финансах и не только.</p>
#             </div>
#             <div class="tech-card">
#                 <div class="tech-icon">
#                     <i class="fas fa-vr-cardboard"></i>
#                 </div>
#                 <a href="http://127.0.0.1:8000/vr"><h3>Виртуальная Реальность</h3></a>
#                 <p>Полное погружение в цифровые миры для обучения, развлечений и удаленной работы с максимальным реализмом.</p>
#             </div>
#             <div class="tech-card">
#                 <div class="tech-icon">
#                     <i class="fas fa-satellite-dish"></i>
#                 </div>
#                 <a href="http://127.0.0.1:8000/iot"><h3>Умные Устройства</h3></a>
#                 <p>Умные устройства, соединенные в единую сеть, автоматизирующие быт, промышленность и городскую инфраструктуру.</p>
#             </div>
#         </div>


@app.get(
    "/link",
)
def root():
    return FileResponse("index.html")


@app.get("https://kounsheng.github.io/MySite/ai")
def ai_page():
    return FileResponse("server_response/files/pages/page_ai.html")


@app.get("/quantum")
def ai_page():
    return FileResponse("server_response/files/pages/page_quantum.html")


@app.get("/genetics")
def ai_page():
    return FileResponse("server_response/files/pages/page_genetics.html")


@app.get("/blockchain")
def ai_page():
    return FileResponse("server_response/files/pages/page_blockchain.html")


@app.get("/vr")
def ai_page():
    return FileResponse("server_response/files/pages/page_vr.html")


@app.get("/iot")
def ai_page():
    return FileResponse("server_response/files/pages/page_iot.html")
