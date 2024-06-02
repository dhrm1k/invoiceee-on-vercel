from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

today = date.today()
strdate = str(today) #Converts input from amount to string to print it below.

@app.route('/ref=producthunt')
def producthunt():
  return redirect(url_for("home.html"))

@app.route("/instructions")
def instructions():
  return render_template("instructions.html")



#Main index that shows how receipt looks without adding the value. No integer present
@app.route('/invoice/<company>/<from1>/<toemail>/<to>/<paymentmethod>/<item1>/<price1>/<item2>/<price2>/<item3>/<price3>/<item4>/<price4>/<item5>/<price5>/')
def mainindex(company=None, from1=None, toemail=None, to=None, item1=None, item2=None, item3=None, item4=None,item5=None, price1=None, price2=None, price3=None, price4=None, paymentmethod=None, price5=None ):

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Invoiceee</title>
<link href="static/new.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
	</head>
	<body>
		<div class="invoice-box">
			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td class="title">
									<img src="https://i.ibb.co/vQCNQHp/Frame-1made-1.png" alt="Frame-1made-1" border="0" style="width: 100%; max-width: 300px"  />
								</td>
								<td>
									
									Created: '''+ strdate +'''<br />
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="information">
					<td colspan="2">
						<table>
							<tr>
								<td>
									''' + company + ''' <br />
                  '''+ from1 +'''<br />
								</td>
								<td>
								'''	+ to + '''<br />
									
								''' + toemail + '''
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="heading">
					<td>Payment Method</td>
					<td></td>
				</tr>
				<tr class="details">
					<td>'''+ paymentmethod +'''</td>
					<td></td>
				</tr>
				<tr class="heading">
					<td>Item</td>
					<td>Price ($)</td>
				</tr>
				<tr class="item">
					<td>'''+ item1 +'''</td>
					<td>'''+ price1 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item2 +'''</td>
					<td>'''+ price2 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item3 +'''</td>
					<td>'''+ price3 +'''</td>
				</tr>
				<tr class="item last">
					<td>'''+ item4 +'''</td>
					<td>'''+ price4 +'''</td>
				</tr>
				<tr class="total">
					<td></td>
					<td>Total:''' ''' 
				</tr>
			</table>
		</div>
	</body>
</html>
  <style>
  .invoice-box {
				max-width: 800px;
				margin: auto;
				padding: 30px;
				border: 1px solid #eee;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}
			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}
			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}
			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}
			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}
			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}
			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}
			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}
			.invoice-box table tr.item.last td {
				border-bottom: none;
			}
			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}
			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}
				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}
			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}
			.invoice-box.rtl table {
				text-align: right;
			}
			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
</style>
</body>
</html>
'''


@app.route('/invoice/<company>/<from1>/<toemail>/<to>/<paymentmethod>/<item1>/<price1>/<item2>/<price2>/<item3>/<price3>/<item4>/<price4>/')
def invoice4items(company=None, from1=None, toemail=None, to=None, item1=None, item2=None, item3=None, item4=None, price1=None, price2=None, price3=None, price4=None, paymentmethod=None ):

  total = int(price1) + int(price2) + int(price3) + int(price4)
  Total = str(total)

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Invoiceee</title>
<link href="static/new.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
	</head>
	<body>
		<div class="invoice-box">
			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td class="title">
										<img src="https://i.ibb.co/vQCNQHp/Frame-1made-1.png" alt="Frame-1made-1" border="0" style="width: 100%; max-width: 300px"  />
								</td>
								<td>
									
									Created: '''+ strdate +'''<br />
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="information">
					<td colspan="2">
						<table>
							<tr>
								<td>
									''' + company + ''' <br />
                  '''+ from1 +'''<br />
								</td>
								<td>
								'''	+ to + '''<br />
									
								''' + toemail + '''
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="heading">
					<td>Payment Method</td>
					<td></td>
				</tr>
				<tr class="details">
					<td>'''+ paymentmethod +'''</td>
					<td></td>
				</tr>
				<tr class="heading">
					<td>Item</td>
					<td>Price ($)</td>
				</tr>
				<tr class="item">
					<td>'''+ item1 +'''</td>
					<td>'''+ price1 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item2 +'''</td>
					<td>'''+ price2 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item3 +'''</td>
					<td>'''+ price3 +'''</td>
				</tr>
				<tr class="item last">
					<td>'''+ item4 +'''</td>
					<td>'''+ price4 +'''</td>
				</tr>
				<tr class="total">
					<td></td>
					<td>Total:'''+ Total + ''' 
				</tr>
			</table>
		</div>
	</body>
</html>
  <style>
  .invoice-box {
				max-width: 800px;
				margin: auto;
				padding: 30px;
				border: 1px solid #eee;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}
			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}
			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}
			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}
			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}
			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}
			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}
			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}
			.invoice-box table tr.item.last td {
				border-bottom: none;
			}
			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}
			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}
				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}
			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}
			.invoice-box.rtl table {
				text-align: right;
			}
			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
</style>
</body>
</html>'''


@app.route('/invoice/<company>/<from1>/<toemail>/<to>/<paymentmethod>/<item1>/<price1>/<item2>/<price2>/<item3>/<price3>/')
def invoice3items(company=None, from1=None, toemail=None, to=None, item1=None, item2=None, item3=None, price1=None, price2=None, price3=None, paymentmethod=None ):
  total = int(price1) + int(price2) + int(price3)
  Total = str(total)

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Invoiceee</title>
<link href="static/new.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
	</head>
	<body>
		<div class="invoice-box">
			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td class="title">
									<img src="https://i.ibb.co/vQCNQHp/Frame-1made-1.png" alt="Frame-1made-1" border="0" style="width: 100%; max-width: 300px"  />
								</td>
								<td>
									
									Created: '''+ strdate +'''<br />
				
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="information">
					<td colspan="2">
						<table>
							<tr>
								<td>
									''' + company + ''' <br />
                  '''+ from1 +'''<br />
								</td>
								<td>
								'''	+ to + '''<br />
									
								''' + toemail + '''
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="heading">
					<td>Payment Method</td>
					<td></td>
				</tr>
				<tr class="details">
					<td>'''+ paymentmethod +'''</td>
					<td></td>
				</tr>
				<tr class="heading">
					<td>Item</td>
					<td>Price ($)</td>
				</tr>
				<tr class="item">
					<td>'''+ item1 +'''</td>
					<td>'''+ price1 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item2 +'''</td>
					<td>'''+ price2 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item3 +'''</td>
					<td>'''+ price3 +'''</td>
				</tr>
				<tr class="total">
					<td></td>
					<td>Total:'''+ Total + ''' 
				</tr>
			</table>
		</div>
	</body>
</html>
  <style>
  .invoice-box {
				max-width: 800px;
				margin: auto;
				padding: 30px;
				border: 1px solid #eee;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}
			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}
			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}
			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}
			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}
			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}
			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}
			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}
			.invoice-box table tr.item.last td {
				border-bottom: none;
			}
			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}
			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}
				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}
			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}
			.invoice-box.rtl table {
				text-align: right;
			}
			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
</style>
</body>
</html>'''


@app.route('/invoice/<company>/<from1>/<toemail>/<to>/<paymentmethod>/<item1>/<price1>/<item2>/<price2>/')
def invoice2items(company=None, from1=None, toemail=None, to=None, item1=None, item2=None, item3=None, item4=None, price1=None, price2=None, paymentmethod=None):
  total = int(price1) + int(price2) 
  Total = str(total)

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Invoiceee</title>
<link href="static/new.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
	</head>
	<body>
		<div class="invoice-box">
			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td class="title">
									<img src="https://i.ibb.co/vQCNQHp/Frame-1made-1.png" alt="Frame-1made-1" border="0" style="width: 100%; max-width: 300px"  />
								</td>
								<td>
									
									Created: '''+ strdate +'''<br />
					
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="information">
					<td colspan="2">
						<table>
							<tr>
								<td>
									''' + company + ''' <br />
                  '''+ from1 +'''<br />
								</td>
								<td>
								'''	+ to + '''<br />
									
								''' + toemail + '''
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="heading">
					<td>Payment Method</td>
					<td></td>
				</tr>
				<tr class="details">
					<td>'''+ paymentmethod +'''</td>
					<td></td>
				</tr>
				<tr class="heading">
					<td>Item</td>
					<td>Price ($)</td>
				</tr>
				<tr class="item">
					<td>'''+ item1 +'''</td>
					<td>'''+ price1 +'''</td>
				</tr>
				<tr class="item">
					<td>'''+ item2 +'''</td>
					<td>'''+ price2 +'''</td>
				</tr>
				<tr class="total">
					<td></td>
					<td>Total:'''+ Total + ''' 
				</tr>
			</table>
		</div>
	</body>
</html>
  <style>
  .invoice-box {
				max-width: 800px;
				margin: auto;
				padding: 30px;
				border: 1px solid #eee;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}
			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}
			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}
			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}
			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}
			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}
			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}
			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}
			.invoice-box table tr.item.last td {
				border-bottom: none;
			}
			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}
			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}
				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}
			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}
			.invoice-box.rtl table {
				text-align: right;
			}
			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
</style>
</body>
</html>''' 


@app.route('/invoice/<company>/<from1>/<toemail>/<to>/<paymentmethod>/<item1>/<price1>/')
def invoice1items(company=None, from1=None, toemail=None, to=None, item1=None, price1=None, paymentmethod=None):
  total = int(price1)
  Total = str(total)

  return '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Invoiceee</title>
<link href="static/new.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
	</head>
	<body>
		<div class="invoice-box">
			<table cellpadding="0" cellspacing="0">
				<tr class="top">
					<td colspan="2">
						<table>
							<tr>
								<td class="title">
									<img src="https://i.ibb.co/vQCNQHp/Frame-1made-1.png" alt="Frame-1made-1" border="0" style="width: 100%; max-width: 300px"  />
								</td>
								<td>
									
									Created: '''+ strdate +'''<br />
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="information">
					<td colspan="2">
						<table>
							<tr>
								<td>
									''' + company + ''' <br />
                  '''+ from1 +'''<br />
								</td>
								<td>
								'''	+ to + '''<br />
									
								''' + toemail + '''
								</td>
							</tr>
						</table>
					</td>
				</tr>
				<tr class="heading">
					<td>Payment Method</td>
					<td></td>
				</tr>
				<tr class="details">
					<td>'''+ paymentmethod +'''+</td>
					<td></td>
				</tr>
				<tr class="heading">
					<td>Item</td>
					<td>Price ($)</td>
				</tr>
				<tr class="item">
					<td>'''+ item1 +'''</td>
					<td>'''+ price1 +'''</td>
				</tr>
	
				</tr>
				<tr class="total">
					<td></td>
					<td>Total:'''+ Total + ''' 
				</tr>
			</table>
		</div>
	</body>
</html>
  <style>
  .invoice-box {
				max-width: 800px;
				margin: auto;
				padding: 30px;
				border: 1px solid #eee;
				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
				font-size: 16px;
				line-height: 24px;
				font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
				color: #555;
			}
			.invoice-box table {
				width: 100%;
				line-height: inherit;
				text-align: left;
			}
			.invoice-box table td {
				padding: 5px;
				vertical-align: top;
			}
			.invoice-box table tr td:nth-child(2) {
				text-align: right;
			}
			.invoice-box table tr.top table td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.top table td.title {
				font-size: 45px;
				line-height: 45px;
				color: #333;
			}
			.invoice-box table tr.information table td {
				padding-bottom: 40px;
			}
			.invoice-box table tr.heading td {
				background: #eee;
				border-bottom: 1px solid #ddd;
				font-weight: bold;
			}
			.invoice-box table tr.details td {
				padding-bottom: 20px;
			}
			.invoice-box table tr.item td {
				border-bottom: 1px solid #eee;
			}
			.invoice-box table tr.item.last td {
				border-bottom: none;
			}
			.invoice-box table tr.total td:nth-child(2) {
				border-top: 2px solid #eee;
				font-weight: bold;
			}
			@media only screen and (max-width: 600px) {
				.invoice-box table tr.top table td {
					width: 100%;
					display: block;
					text-align: center;
				}
				.invoice-box table tr.information table td {
					width: 100%;
					display: block;
					text-align: center;
				}
			}
			/** RTL **/
			.invoice-box.rtl {
				direction: rtl;
				font-family: Tahoma, 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif;
			}
			.invoice-box.rtl table {
				text-align: right;
			}
			.invoice-box.rtl table tr td:nth-child(2) {
				text-align: left;
			}
</style>
</body>
</html>'''


if __name__ == "__main__":
  app.run(debug=True)