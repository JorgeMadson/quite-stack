# save_to_db.py
from datetime import datetime
from models import Session, MessageStatus

def salva_messagem_por_status(data):
    session = Session()

    # Verifica se a chave 'results' está no JSON
    if 'results' in data:
        for result in data['results']:
            message_status = MessageStatus(
                bulk_id=result.get('bulkId'),
                message_id=result.get('messageId'),
                status_group=result['status'].get('groupName'),
                status_name=result['status'].get('name'),
                status_description=result['status'].get('description'),
                error_id=result['error'].get('id'),
                error_name=result['error'].get('name'),
                error_description=result['error'].get('description'),
                error_group=result['error'].get('groupName'),
                error_permanent=result['error'].get('permanent'),
                price_per_message=result['price'].get('pricePerMessage'),
                currency=result['price'].get('currency'),
                done_at=datetime.strptime(result.get('doneAt'), '%Y-%m-%dT%H:%M:%S.%f%z') if result.get('doneAt') else None,
                sent_at=datetime.strptime(result.get('sentAt'), '%Y-%m-%dT%H:%M:%S.%f%z') if result.get('sentAt') else None,
                sms_count=result.get('smsCount'),
                callback_data=result.get('callbackData'),
                recipient=result.get('to')
            )
            session.add(message_status)

    session.commit()
    session.close()