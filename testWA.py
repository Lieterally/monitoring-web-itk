import requests

def send_whatsapp(phone_number: str, description: str, status: str):
    url = 'https://wa01.ocatelkom.co.id/api/v2/push/message'
    
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiYXBwbGljYXRpb24iOiI2NWE4OTYwYTBmYWJhYzAwMTkyZTY2MzciLCJpYXQiOjE1MTYyMzkwMjJ9.OiZekdcoFNPLmjtCgjTtfH_HQ6h8BjrxnxxwV_0jO8Bcc2jUyJclLHCh5DeY1XAOugrgPEdA1Gt_RU8Dy9CWzpFAWbJUMrjkievzT5FKSdGXBUpstIsQyTWNL00fhXB1Tss14gxSD2_vCguNZb-6qynbUg_93kg4TJdu7W3Lfa_fZLtWvwewTkqnDUPU6YwHGAsHIxDwM1M-DsWJnJy346lZlsAYJQKl_TTYHypCThbNvHBsBJQTsAfR4oE1O0qfZCyJIo7Hmj_hMgseVLSdlDzs3CSV9VlFnRsdRvIncANfc49yGIWizbVejsAwNiuSfdxh5ovp294EqjqjoPCM7w',
        'Content-Type': 'application/json'
    }

    payload = {
        "phone_number": phone_number,
        "message": {
            "type": "template",
            "template": {
                "template_code_id": "d7529850_b0a9_41fe_b49c_b7d78ed184de:notif_monitoring_copy1",
                "payload": [
                    {
                        "position": "body",
                        "parameters": [
                            {"type": "text", "text": description},
                            {"type": "text", "text": status}
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.text

if __name__ == "__main__":
    print("=== WhatsApp Monitoring Notifier ===")
    phone = input("Enter phone number (e.g. 6281234567890): ").strip()
    desc = input("Enter description: ").strip()
    status = input("Enter status: ").strip()

    print("\nSending message...")
    result = send_whatsapp(phone, desc, status)
    print("Response:\n", result)