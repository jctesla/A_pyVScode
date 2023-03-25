# Keep this file separate

# https://apps.twitter.com/
# Create new App and get the four strings

def oauth():
    key = 1
    
    # ususario del profe
    if key==0:
        return {"consumer_key": "h7Lu...Ng",
                "consumer_secret": "dNKenAC3New...mmn7Q",
                "token_key": "10185562-eibxCp9n2...P4GEQQOSGI",
                "token_secret": "H0ycCFemmC4wyf1...qoIpBo"}

    # mi usuario
    if key==1:
        return {"consumer_key": "UHKdjrdb7QzPrRO3pEwDJkZPC",
                "consumer_secret": "2ieZgzh6n1YrjNjrsjDgSK0F1dx9oltQl8cfMF1DMbn1CoG3ui",
                "token_key": "723972523-5FQRsCwvd8V4MU6kE08ILHdFiayeqzM6KSfXl1ga",
                "token_secret": "lMznDS9jX9EDHRYTrgXu6Qdh3ZXOWn6NQds0EIFEXWsJi"}



#nota:
    # p Generar Consumer_key/_secret & tocken_key/_secret:
    # Ingrese a https://dev.twitter.com/ e ingrese con su usuario de twitter
    # Luego ingrese a https://dev.twitter.com/apps/new