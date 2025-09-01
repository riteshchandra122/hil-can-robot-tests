# can_utils.py
import can

def send_can_message(arbitration_id, data):
    """
    Send a CAN message.
    arbitration_id: hex string like '0x123'
    data: hex string like '0A0B0C0D'
    """
    # using virtual bus for practice (no hardware)
    bus = can.interface.Bus(bustype='virtual')
    msg = can.Message(arbitration_id=int(arbitration_id, 16),
                      data=bytes.fromhex(data),
                      is_extended_id=False)
    bus.send(msg)
    return f"Message sent: ID={arbitration_id}, Data={data}"

def receive_can_message(timeout=2):
    """
    Receive a CAN message with a timeout (seconds).
    """
    bus = can.interface.Bus(bustype='virtual')
    msg = bus.recv(timeout)
    if msg:
        return f"Received: ID={hex(msg.arbitration_id)}, Data={msg.data.hex()}"
    else:
        return "No message received"
