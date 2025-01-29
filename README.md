# Desafio de Programação: API de Envio de Email

Este projeto consiste em desenvolver uma API utilizando Flask, SQLAlchemy e Celery para gerenciar o envio de emails e suas respectivas respostas. O objetivo é criar uma aplicação que receba informações de um serviço externo e armazene os dados relevantes em um banco de dados.

## Tecnologias Utilizadas

- **Flask**: Framework web para construir a API.
- **SQLAlchemy**: ORM (Object Relational Mapping) para interagir com o banco de dados.
- **Celery**: Biblioteca para tarefas assíncronas.

## Funcionalidades

1. **Receber Payload**: A API deve receber um POST na rota `/email` com os dados do serviço de envio de email.
2. **Processamento Assíncrono**: Os dados recebidos devem ser enviados para uma fila (email-webhook) para processamento assíncrono.
3. **Armazenamento no Banco**: Uma função deve inserir a entidade `email_callback` no banco de dados SQLite, contendo as seguintes informações:
   - `status`: Status do email (ex.: DELIVERED, UNDELIVERABLE).
   - `email`: Endereço de email.
   - `data do recebimento`: Data em que a resposta foi recebida.
   - `id externo`: Identificador único para cada retorno.
   - `qj_contact_id`: ID interno da aplicação.

### Estrutura da Entidade `email_callback`

| Campo            | Tipo        | Descrição                                         |
|------------------|-------------|---------------------------------------------------|
| status           | String      | Status do email (ex.: DELIVERED, UNDELIVERABLE)   |
| email            | String      | Endereço de email                                 |
| data_recebimento | DateTime    | Data do recebimento da resposta                   |
| id_externo       | String      | ID externo para identificar cada retorno          |
| qj_contact_id    | Integer     | ID interno da aplicação                           |

### Exemplo de Payload

```python
exemplos de retorno:

    'DELIVERED': {'results': [{'bulkId': '7dy3rajfsn3en76hsztl', 'price': {'pricePerMessage': 0.001, 'currency': 'BRL'}, 'status': {'id': 5, 'groupId': 3, 'groupName': 'DELIVERED', 'name': 'DELIVERED_TO_HANDSET', 'description': 'Message delivered to handset'}, 'error': {'id': 0, 'name': 'NO_ERROR', 'description': 'No Error', 'groupId': 0, 'groupName': 'OK', 'permanent': False}, 'messageId': 'yfkgy9xol5kpl33u384n', 'doneAt': '2024-07-16T17:26:54.966-0300', 'smsCount': 1, 'sentAt': '2024-07-16T17:26:52.880-0300', 'browserLink': '', 'callbackData': '{"qj_contact_id": 3}', 'to': 'joao.madero@quite.com.br'}]},
    'UNDELIVERABLE': {'results': [{'bulkId': 'u38ifa6y5hsjyacodpyn', 'price': {'pricePerMessage': 0.0, 'currency': 'BRL'}, 'status': {'id': 4, 'groupId': 2, 'groupName': 'UNDELIVERABLE', 'name': 'UNDELIVERABLE_REJECTED_OPERATOR', 'description': 'Message rejected by operator'}, 'error': {'id': 6012, 'name': 'EC_SENDER_ADDRESS_INVALID', 'description': 'Sending address invalid, possible syntax error', 'groupId': 1, 'groupName': 'HANDSET_ERRORS', 'permanent': True}, 'messageId': 'vzl7uvqhq7lt1fa66718', 'doneAt': '2024-07-16T17:15:21.288-0300', 'smsCount': 1, 'sentAt': '2024-07-16T17:15:21.286-0300', 'callbackData': '{"qj_contact_id": 3}', 'to': 'joao.madero@quite.com.br'}]},
    'SUPPRESSED_BOUNCE': {'bulkId': 'svulxb6rjqajapkmvyvy', 'price': {'pricePerMessage': 0.0025, 'currency': 'BRL'}, 'status': {'id': 4, 'groupId': 2, 'groupName': 'UNDELIVERABLE', 'name': 'UNDELIVERABLE_REJECTED_OPERATOR', 'description': 'Message rejected by operator'}, 'error': {'id': 6034, 'name': 'EC_SUPPRESSED_BOUNCE', 'description': 'Recipient address suppressed due to bounce', 'groupId': 1, 'groupName': 'HANDSET_ERRORS', 'permanent': True}, 'messageId': '1955tld5lqf3mn9ou3tz', 'doneAt': '2024-09-03T15:10:44.395-0300', 'smsCount': 1, 'sentAt': '2024-09-03T15:10:44.294-0300', 'callbackData': '{"qj_approach_flow_id": "35", "qj_approach_flow_name": "[EMAIL] L - Fluxo Sem Interações", "qj_approach_flow_campaign": "Setembro/2024_sem_interações", "qj_contact_id": "310372388", "qj_creditor_id": "2", "qj_creditor_name": "Quite", "qj_customer_id": "43816741", "qj_stimulus_hot": "1", "qj_approach_offset": "1", "qj_snapshot": "6892059880", "qj_subject": "Paulo, você foi contemplado com uma condição especial Geru! \\ud83c\\udf81", "qj_deal_id": "88921261", "qj_stimulus_history_id": "408", "qj_firing_id": 485456}', 'to': 'paulorobetovlopes@hotmail.com'},
    'OPENED': {'notificationType': 'OPENED', 'domain': 'negociecomquite.com.br', 'recipient': 'joao.madero@quite.com.br', 'sendDateTime': 1721161444325, 'messageId': '3nghqee2ktl9c6ta3z56', 'bulkId': 'o22v6rmvov7bdigol2n4', 'callbackData': '{"qj_contact_id": 3}', 'recipientInfo': {'deviceType': 'Desktop', 'os': 'Windows XP', 'deviceName': 'PC'}, 'geoLocationInfo': {'countryName': 'United States', 'city': 'Mountain View'}},
    'CLICKED': {'notificationType': 'CLICKED', 'domain': 'negociecomquite.com.br', 'recipient': 'joao.madero@quite.com.br', 'url': 'www.google.com?utm_medium=email', 'sendDateTime': 1721161640510, 'messageId': 'yfkgy9xol5kpl33u384n', 'bulkId': '7dy3rajfsn3en76hsztl', 'callbackData': '{"qj_contact_id": 3}', 'recipientInfo': {'deviceType': 'Desktop', 'os': 'Unknown', 'deviceName': 'PC'}, 'geoLocationInfo': {'countryName': 'Brazil', 'city': 'Sao Paulo'}},
    'UNSUBSCRIBED': {"notificationType": "UNSUBSCRIBED", "domain": "some-domain.com", "recipient": "john.doe@some-domain.com", "sendDateTime": 1704106800000, "messageId": "14b734recsf69n8zkao5", "bulkId": "ikzzmbhu6223bxkhmyrj", "callbackData": '{"qj_contact_id": 3}', "recipientInfo": {"deviceType": "Phone", "os": "iOS 12", "deviceName": "Apple"}, "geoLocation": {"city": "Los Angeles", "countryName": "United States"}},
    'COMPLAINED': { "notificationType": "COMPLAINED", "domain": "some-domain.com", "recipient": "john.doe@some-domain.com", "sendDateTime": 1704106800000, "messageId": "14b734recsf69n8zkao5", "bulkId": "ikzzmbhu6223bxkhmyrj", "callbackData": '{"qj_contact_id": 3}'},
    'DELIVERED_DICT': {"results": [{"bulkId": "fsfrqsxr66vigdfltnpz","price": { "pricePerMessage": 0.0025, "currency": "BRL"},"status": { "id": 5, "groupId": 3, "groupName": "DELIVERED", "name": "DELIVERED_TO_HANDSET", "description": "Message delivered to handset"},"error": { "id": 0, "name": "NO_ERROR", "description": "No Error", "groupId": 0, "groupName": "OK", "permanent": False},"messageId": "jymy9kls8qx59blkizg4","doneAt": "2024-08-07T08:43:07.621-0300","smsCount": 1,"sentAt": "2024-08-07T08:43:05.627-0300","browserLink": "","callbackData": "{'qj_approach_flow_id': '1783', 'qj_approach_flow_name': '[aquecimento]', 'qj_approach_flow_campaign': 'aquecimento', 'qj_contact_id': '124127953', 'qj_creditor_id': '13', 'qj_creditor_name': 'Geru', 'qj_customer_id': '39100489', 'qj_stimulus_hot': '1', 'qj_approach_offset': '1', 'qj_snapshot': '11038928605', 'qj_subject': 'Alexandre, agora voc\\u00ea pode contar com a QuiteJ\\u00e1 para dar adeus a pend\\u00eancia Geru!', 'qj_deal_id': '173084073', 'qj_stimulus_history_id': '1546277', 'qj_firing_id': 489166}","to": "xbbvalle@mail.com"},{"bulkId": "u13d2uoz3z4j43kbdyfu","price": { "pricePerMessage": 0.0025, "currency": "BRL"},"status": { "id": 5, "groupId": 3, "groupName": "DELIVERED", "name": "DELIVERED_TO_HANDSET", "description": "Message delivered to handset"},"error": { "id": 0, "name": "NO_ERROR", "description": "No Error", "groupId": 0, "groupName": "OK", "permanent": False},"messageId": "e8d7z6zlm8o88t7k58qi","doneAt": "2024-08-07T08:43:07.547-0300","smsCount": 1,"sentAt": "2024-08-07T08:43:05.902-0300","browserLink": "","callbackData": "{'qj_approach_flow_id': '1783', 'qj_approach_flow_name': '[aquecimento]', 'qj_approach_flow_campaign': 'aquecimento', 'qj_contact_id': '111372120', 'qj_creditor_id': '13', 'qj_creditor_name': 'Geru', 'qj_customer_id': '33463879', 'qj_stimulus_hot': '1', 'qj_approach_offset': '1', 'qj_snapshot': '5901886909', 'qj_subject': 'Thiago, agora voc\\u00ea pode contar com a QuiteJ\\u00e1 para dar adeus a pend\\u00eancia Geru!', 'qj_deal_id': '193175357', 'qj_stimulus_history_id': '1546277', 'qj_firing_id': 489166}","to": "thiagocsfoz@mail.com"},{"bulkId": "p7tfqzt6kiaj2sabheaj","price": { "pricePerMessage": 0.0025, "currency": "BRL"},"status": { "id": 5, "groupId": 3, "groupName": "DELIVERED", "name": "DELIVERED_TO_HANDSET", "description": "Message delivered to handset"},"error": { "id": 0, "name": "NO_ERROR", "description": "No Error", "groupId": 0, "groupName": "OK", "permanent": False},"messageId": "1ruocbp8ccqv1sx2k7uy","doneAt": "2024-08-07T08:43:07.564-0300","smsCount": 1,"sentAt": "2024-08-07T08:43:05.903-0300","browserLink": "","callbackData": "{'qj_approach_flow_id': '1783', 'qj_approach_flow_name': '[aquecimento]', 'qj_approach_flow_campaign': 'aquecimento', 'qj_contact_id': '208821129', 'qj_creditor_id': '13', 'qj_creditor_name': 'Geru', 'qj_customer_id': '45895586', 'qj_stimulus_hot': '1', 'qj_approach_offset': '1', 'qj_snapshot': '2079960083', 'qj_subject': 'Luis, agora voc\\u00ea pode contar com a QuiteJ\\u00e1 para dar adeus a pend\\u00eancia Geru!', 'qj_deal_id': '122268724', 'qj_stimulus_history_id': '1546277', 'qj_firing_id': 489166}","to": "lgg.noia@mail.com"},{"bulkId": "k1msf8rhepnazoi52c7c","price": { "pricePerMessage": 0.0025, "currency": "BRL"},"status": { "id": 5, "groupId": 3, "groupName": "DELIVERED", "name": "DELIVERED_TO_HANDSET", "description": "Message delivered to handset"},"error": { "id": 0, "name": "NO_ERROR", "description": "No Error", "groupId": 0, "groupName": "OK", "permanent": False},"messageId": "rap1yuru9sy6rktvgq77","doneAt": "2024-08-07T08:43:07.575-0300","smsCount": 1,"sentAt": "2024-08-07T08:43:05.870-0300","browserLink": "","callbackData": "{'qj_approach_flow_id': '1783', 'qj_approach_flow_name': '[aquecimento]', 'qj_approach_flow_campaign': 'aquecimento', 'qj_contact_id': '277652016', 'qj_creditor_id': '13', 'qj_creditor_name': 'Geru', 'qj_customer_id': '41771150', 'qj_stimulus_hot': '1', 'qj_approach_offset': '1', 'qj_snapshot': '46348910857', 'qj_subject': 'Thiago, agora voc\\u00ea pode contar com a QuiteJ\\u00e1 para dar adeus a pend\\u00eancia Geru!', 'qj_deal_id': '181035514', 'qj_stimulus_history_id': '1546277', 'qj_firing_id': 489166}","to": "thiagogiatti0@mail.com"},{"bulkId": "mprhxcn1g79hhi4hyops","price": { "pricePerMessage": 0.0025, "currency": "BRL"},"status": { "id": 5, "groupId": 3, "groupName": "DELIVERED", "name": "DELIVERED_TO_HANDSET", "description": "Message delivered to handset"},"error": { "id": 0, "name": "NO_ERROR", "description": "No Error", "groupId": 0, "groupName": "OK", "permanent": False},"messageId": "hikah5b6b3hfqocz5bux","doneAt": "2024-08-07T08:43:07.582-0300","smsCount": 1,"sentAt": "2024-08-07T08:43:05.891-0300","browserLink": "","callbackData": "{'qj_approach_flow_id': '1783', 'qj_approach_flow_name': '[aquecimento]', 'qj_approach_flow_campaign': 'aquecimento', 'qj_contact_id': '261041888', 'qj_creditor_id': '13', 'qj_creditor_name': 'Geru', 'qj_customer_id': '41263238', 'qj_stimulus_hot': '1', 'qj_approach_offset': '1', 'qj_snapshot': '38043996814', 'qj_subject': 'Kevim, agora voc\\u00ea pode contar com a QuiteJ\\u00e1 para dar adeus a pend\\u00eancia Geru!', 'qj_deal_id': '197563808', 'qj_stimulus_history_id': '1546277', 'qj_firing_id': 489166}","to": "luisgomes@mail.com"}]}
```

TODO
----

1.  **Implementar a API**:
    
    *   Criar o endpoint /email utilizando Flask.
        
    *   Verificar se está recebendo e imprimindo corretamente os dados.
        
2.  **Função para Inserção no Banco**:
    
    *   Criar uma função que receba o payload e insira os dados no banco usando SQLAlchemy.
        
3.  **Configurar Celery**:
    
    *   Criar uma fila para executar a função de forma assíncrona.
        

Como Executar o Projeto
-----------------------

1.  pip install Flask SQLAlchemy Celery
    
2.  flask run
    
3.  celery -A seu\_modulo worker --loglevel=info
    

Contribuições
-------------

Sinta-se à vontade para contribuir com melhorias ou correções neste projeto!
