# Python Multithreaded Port Scanner

Um scanner de portas TCP desenvolvido em **Python** que utiliza **multithreading** para realizar análises rápidas e eficientes. A ferramenta permite verificar um intervalo de portas num determinado host, identificando as portas abertas e o respetivo serviço quando disponível.

> **Nota:** Este projeto foi desenvolvido para fins educativos e deve ser utilizado apenas em sistemas para os quais exista autorização.

---

## Funcionalidades

- Scan de portas TCP.
- Definição de intervalo de portas personalizado.
- Execução multithread para maior desempenho.
- Identificação do serviço associado à porta.
- Barra de progresso durante o scan.
- Medição do tempo total de execução.

---

## Tecnologias

- Python 3
- Socket
- concurrent.futures (ThreadPoolExecutor)
- tqdm

---

## Requisitos

- Python 3.8 ou superior

Instale a dependência:

```bash
pip install tqdm
```
## Screenshot

<p align="center">
  <img src="images/prtsc1.png" alt="Port Scanner" width="800">
</p>

<p align="center">
  <img src="images/prtsc.png" alt="Port Scanner" width="800">
</p>
