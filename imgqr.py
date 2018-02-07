import qrcode
import image

def code(info):
    qr = qrcode.QRCode()
    qr.add_data(
       '''
        BEGIN:VCARD\n
        VERSION:3.0\n
        FN:%s\n
        TEL:%s\n
        END:VCARD
       ''' %(info[0],info[1])
    )
    img = qr.make_image()
    img.save('F:\zc\LFZ1.png')

code(['li','13311111111'])


