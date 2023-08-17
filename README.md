## ExcelConsolidator: RH Edition 📊

### Descrição:

**ExcelConsolidator: RH Edition** é uma ferramenta Python desenvolvida para simplificar e automatizar a tarefa de consolidar múltiplos arquivos Excel contendo dados de absenteísmo. Composta por dois módulos principais, a ferramenta fornece um método fácil e eficiente para gerar e consolidar dados de ausências.

### Módulos Principais:

#### 1. Consolidador 🚀

Este módulo é responsável por:

* Consolidar múltiplos arquivos Excel em um único arquivo.
* Utilizar a biblioteca `pandas` para garantir eficiência na consolidação.
* Organizar automaticamente os dados consolidados em uma pasta específica.

#### 2. Generator 📑

Este módulo:

* Gera arquivos Excel mockados com dados de absenteísmo.
* Usa a biblioteca `faker` para criar dados realistas.
* Permite simular cenários reais e testar a eficiência do módulo Consolidador.

### Como Utilizar:

1. Clone o repositório:
    
    ```bash
    git clone https://github.com/lvgalvao/ExcelConsolidator.git
    ```
    
2. Mova-se para o diretório e instale as dependências:
    
    ```bash
    cd ExcelConsolidator
    pip install -r requirements.txt
    ```
    
3. Execute o script principal:
    
    ```css
    python main.py
    ```
    