import qrcode

upi_id =input("entr your upi id =")

phonepe_url =f' upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f' upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url =f' upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr =qrcode.make(phonepe_url)
paytm_qr =qrcode.make(paytm_url)
google_pay_qr =qrcode.make(google_pay_url)


phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

phonepe_qr.imshow()
paytm_qr.imshow()
google_pay_qr.imshow()
