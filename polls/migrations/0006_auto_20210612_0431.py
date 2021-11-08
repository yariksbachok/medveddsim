# Generated by Django 3.2.4 on 2021-06-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_alter_numberssssq_shirt_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=100)),
                ('photo_company', models.ImageField(upload_to='photo/%Y/%m/&d/')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.AlterField(
            model_name='numberssssq',
            name='shirt_company',
            field=models.CharField(choices=[('1St', '1StopMove'), ('Abr', 'AccountPatrol'), ('Aff', 'Affirm'), ('Aft', 'AfterPay'), ('Air', 'AirBnB'), ('Alb', 'Albert'), ('ALI', 'Alibaba'), ('AMA', 'Amazon'), ('AND', 'Ando'), ('AOL', 'AOL'), ('APP', 'Apple'), ('AT&', 'AT&T'), ('ATO', 'Atom'), ('AAXO', 'AxosBank'), ('BAN', 'Banxa'), ('BAN', 'Banq'), ('BAS', 'BaskBank'), ('BB&', 'BB&T'), ('BBV', 'BBVA'), ('BEF', 'BeFrugal'), ('BET', 'Betterment'), ('BES', 'BestBuy'), ('BIG', 'BigoLive'), ('BIT', 'Bit2Me'), ('BIN', 'Binance'), ('BIY', 'BitFlyer'), ('BIL', 'BitLeague'), ('BIM', 'Bitmo'), ('BIR', 'Bitfront'), ('BLA', 'BlackPeopleMeet'), ('BIA', 'Bitstamp'), ('BLV', 'BlueVine'), ('BLO', 'BlockFi'), ('BOF', 'BOFA'), ('BOO', 'Booking'), ('BOS', 'Boss'), ('BOX', 'BoxyPay'), ('BRE', 'Brex'), ('BRA', 'Bread'), ('BUD', 'Bundil'), ('BUN', 'BunQ'), ('BUR', 'Burner'), ('CAP', 'CapitalOne'), ('CAR', 'CardCookie'), ('CAD', 'CardDelivery'), ('CSH', 'CashApp'), ('CDK', 'CDkeys'), ('CEX', 'Cex.io'), ('CHA', 'Chase'), ('CHB', 'CheckBook'), ('CHM', 'Chemistry'), ('CHI', 'Chime'), ('CIR', 'Circle'), ('CIT', 'CITBank'), ('CIB', 'CitiBank'), ('CJS', 'cjsCDkeys'), ('COG', 'Cogni'), ('CON', 'CoinBase'), ('COD', 'CoinField'), ('COP', 'CoinFlip'), ('COH', 'CoinHouseSAS'), ('COB', 'CoinsBank'), ('COE', 'Coinseed'), ('COS', 'CoinSmart'), ('COZ', 'CoinZoom'), ('COR', 'Craigslist'), ('COK', 'CreditKarma'), ('COI', 'CreditSesame'), ('COC', 'Crypto'), ('COV', 'CryptoVoucher'), ('COU', 'Current'), ('CVE', 'Curve'), ('CAV', 'Dave'), ('CCU', 'DCU'), ('CHL', 'DHL'), ('CAL', 'Dialpad'), ('CIG', 'Digit'), ('CSN', 'Ding'), ('CDV', 'DiscoverBank'), ('DOO', 'DoorDash'), ('DUC', 'DocuSign'), ('DUN', 'DunkinDonuts'), ('DYN', 'Dynadot'), ('EAE', 'EA'), ('EBA', 'Ebay'), ('EGI', 'eGifter'), ('ENA', 'Eneba'), ('ENR', 'EnergiEarndrop'), ('EPA', 'ePayments'), ('ERE', 'eRewards'), ('ETO', 'eToro'), ('FAC', 'Facebook'), ('FED', 'FedEx'), ('FID', 'FidelityInvestments'), ('FIN', 'Fin.do'), ('FIR', 'FirstIB'), ('FIV', 'Fiverr'), ('FLI', 'Flir'), ('FLU', 'Fluz'), ('FNB', 'FNB'), ('G2A', 'G2A'), ('GAM', 'GameFlip'), ('GEM', 'Gemini/Authy'), ('GIF', 'Giftnix'), ('GLA', 'GlanceCapital'), ('GOB', 'GoBank/GreenDot'), ('GOO', 'Google'), ('GOP', 'GooglePay'), ('FOV', 'Google Voic'), ('GRA', 'Grailed'), ('GRE', 'Greenlight'), ('HEL', 'Helcim'), ('HOM', 'HomeAway/VRBO'), ('HUG', 'Huggies'), ('HUN', 'Huntington'), ('ICQ', 'ICQ'), ('IDM', 'ID.me'), ('IHE', 'iHerb'), ('IMO', 'Imo'), ('COS', 'Indi'), ('COS', 'Instagram'), ('COS', 'InstaRem'), ('COS', 'Intuit'), ('COS', 'Intermex'), ('COS', 'IPserver.su'), ('COS', 'Jelli'), ('COS', 'Jerry'), ('COS', 'JobStack/PeopleReady'), ('COS', 'JoinToken'), ('COS', 'Juno'), ('COS', 'Katapult'), ('COS', 'KakaoTalk'), ('COS', 'KeyBank'), ('COS', 'Keybase'), ('COS', 'Kixify'), ('COS', 'Klarna'), ('COS', 'Kontalk'), ('COS', 'KYC'), ('COS', 'LBRY'), ('COS', 'Level'), ('COS', 'Line'), ('COS', 'Linen'), ('COS', 'LiveOakBank'), ('COS', 'LinkedIn'), ('COS', 'LocalBitcoins'), ('COS', 'Loftit'), ('COS', 'Lyft'), ('COS', 'Lykke'), ('COS', 'Mailgun'), ('COS', 'M1Finance'), ('COS', 'Marcus'), ('COS', 'Match'), ('COS', 'Mercari'), ('COS', 'Mercuryo'), ('COS', 'Mesh'), ('COS', 'MetalPay'), ('COS', 'Mezu'), ('COS', 'Microsoft'), ('COS', 'Mint'), ('COS', 'MoCaFi'), ('COS', 'MoneyLion'), ('COS', 'MoneyPack'), ('COS', 'MoonPay'), ('COS', 'MOVO'), ('COS', 'MuleFactory'), ('COS', 'MyPoints'), ('COS', 'MyTime'), ('COS', 'MyWallet'), ('COS', 'NavyFederal'), ('COS', 'NBKC'), ('COS', 'NerdWallet'), ('COS', 'Netflix'), ('COS', 'NetZero'), ('COS', 'Newegg'), ('COS', 'Nike'), ('COS', 'NorthOne'), ('COS', 'Novo'), ('COS', 'OceanFirstBank'), ('COS', 'OfferUp'), ('COS', 'OffGamers'), ('COS', 'OFX'), ('COS', 'One'), ('COS', 'OneMain'), ('COS', 'OneGold'), ('COS', 'OnlineCheckWriter'), ('COS', 'OnJuno'), ('COS', 'OnlyFans'), ('COS', 'Oobit'), ('COS', 'Oxygen'), ('COS', 'Pangea'), ('COS', 'Passbook'), ('COS', 'Passfolio'), ('COS', 'Paxful'), ('COS', 'Paynote'), ('COS', 'Payoneer'), ('COS', 'PayPal'), ('COS', 'PaySend'), ('COS', 'PayThem'), ('COS', 'PCGameSupply'), ('COS', 'pCloudy'), ('COS', 'Petal'), ('COS', 'PingID'), ('COS', 'Place'), ('COS', 'Plastiq'), ('COS', 'PlayAsia'), ('COS', 'PlayerAuctions'), ('COS', 'PlayersLounge'), ('COS', 'PNC Bank'), ('COS', 'PoderCard'), ('COS', 'PoF'), ('COS', 'Point'), ('COS', 'PopAds'), ('COS', 'PopMoney'), ('COS', 'Postmates'), ('COS', 'Privacy'), ('COS', 'PropellersAds'), ('COS', 'ProtonMail'), ('COS', 'Pruvit'), ('COS', 'QuadPay'), ('COS', 'QubeMoney'), ('COS', 'QuickBooks'), ('COS', 'Radius'), ('COS', 'Raise'), ('COS', 'Razer'), ('COS', 'RegionsBank'), ('COS', 'Remitly'), ('COS', 'Remmesa'), ('COS', 'Revolut'), ('COS', 'RiaFinancial'), ('COS', 'RobinHood'), ('COS', 'RRF'), ('COS', 'SafeCurrency'), ('COS', 'Schwab'), ('COS', 'SeaGM'), ('COS', 'SendWave'), ('COS', 'Sezzle'), ('COS', 'Sfox'), ('COS', 'Shipito'), ('COS', 'Shopify'), ('COS', 'ShopPay'), ('COS', 'Signal'), ('COS', 'SiguePay'), ('COS', 'Simple'), ('COS', 'SimpleTexting'), ('COS', 'SimplexCC'), ('COS', 'Skrill'), ('COS', 'Slide'), ('COS', 'Snap'), ('COS', 'Snap'), ('COS', 'Snap'), ('COS', 'SoFy'), ('COS', 'Spectrum'), ('COS', 'Spot'), ('COS', 'Stamps'), ('COS', 'Stash'), ('COS', 'Steam'), ('COS', 'Step'), ('COS', 'Stilt'), ('COS', 'Strike'), ('COS', 'Stripe'), ('COS', 'Surplus'), ('COS', 'Switchere'), ('COS', 'SwagBucks'), ('COS', 'Target'), ('COS', 'TDBank'), ('COS', 'Telegram'), ('COS', 'TicketMaster'), ('COS', 'Tinder'), ('COS', 'TorFX'), ('COS', 'TransferMate'), ('COS', 'TransferWise'), ('COS', 'TurboTax'), ('COS', 'TurboTenant'), ('COS', 'Turo'), ('COS', 'Twilio'), ('COS', 'Twitter'), ('COS', 'Uber'), ('COS', 'Uphold'), ('COS', 'UPS'), ('COS', 'Upwork'), ('COS', 'USAA'), ('COS', 'U.S.Bank'), ('COS', 'Vanguard'), ('COS', 'Varo'), ('COS', 'Venmo'), ('COS', 'Viber'), ('COS', 'VictoriaMilan'), ('COS', 'VidaPlayer'), ('COS', 'Vinted'), ('COS', 'VK.com'), ('COS', 'Waleteros'), ('COS', 'Walmart'), ('COS', 'Wealthfront'), ('COS', 'Webull'), ('COS', 'WeChat'), ('COS', 'WellsFargo'), ('COS', 'WhatsApp'), ('COS', 'Wicket'), ('COS', 'WickrMe'), ('COS', 'Wire'), ('COS', 'Womply'), ('COS', 'WWTBAM'), ('COS', 'Wyre'), ('COS', 'XAPO'), ('COS', 'Xcoins'), ('COS', 'Xfinity'), ('COS', 'Xoom'), ('COS', 'Yahoo'), ('COS', 'Yandex'), ('COS', 'Yodlee.Money'), ('COS', 'YouTube'), ('COS', 'Zacks'), ('COS', 'Zadarma'), ('COS', 'Zangi'), ('COS', 'Zapier'), ('COS', 'Zapier'), ('COS', 'Zelle'), ('COS', 'Zero'), ('COS', '*********BN'), ('COS', 'Zillow')], default='App', max_length=15),
        ),
    ]
