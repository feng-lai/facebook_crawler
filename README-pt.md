
[English](README.md) | [日本語](README-jp.md) | [العربية](README-ar.md) | [Português](README-pt.md) | [Español](README-es.md)

# Instruções de uso do Facebook Crawler

## 1. Instalar bibliotecas dependentes

```bash
pip install -r requirements.txt
````

## 2. Configurar o `facebook.exe`

### Preencher a senha da conta

Preencha seu nome de usuário e senha do Facebook no local designado no código:

```python
# Exemplo (substitua o conteúdo entre aspas)
username = "your_username"
password = "your_password"
```

### Substituir o link do grupo

Substitua o link no código pelo link do grupo alvo que você deseja rastrear:

```python
# Exemplo (substitua pelo link real do grupo)
group_url = " https://www.facebook.com/groups/your_target_group "
```

### Definir quantidade de rastreamento (opcional)

Se desejar limitar a quantidade de dados rastreados, modifique os dois números a seguir:

```python
# Exemplo (modifique o número para a quantidade desejada)
while len(data) < 98:
```

```python
# Exemplo (modifique o número para a quantidade desejada)
if len(data) >= 98:
```

## 3. Lidando com situações que requerem operação manual

### Fechamento de janela pop-up

Se aparecer a janela pop-up a seguir, feche manualmente:
[![1.png](https://i.postimg.cc/Gt1LCdJn/1.png)](https://postimg.cc/2b2RdpK0)
[![2.png](https://i.postimg.cc/9FbW63Ds/2.png)](https://postimg.cc/F7f5SBgx)

### Atualizar página

Se houver problema no carregamento da página, atualize manualmente:
[![3.png](https://i.postimg.cc/CKBSnzcV/3.png)](https://postimg.cc/v1sppHRP)

### Processamento do código de verificação

Se encontrar um código de verificação por imagem, preencha conforme as instruções na página, o programa continuará executando sem sair.

## 4. Mensagem de conclusão

Quando a seguinte saída for exibida, significa que o rastreamento foi concluído:

```python
"Data saved to .......csv"
```


