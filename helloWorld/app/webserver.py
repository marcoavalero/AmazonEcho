import ssl 

'''
Generate a private key:
    openssl genrsa -des3 -out server.key 1024

    Generate a CSR
    openssl req -new -key server.key -out server.csr

    Remove Passphrase from key
    cp server.key server.key.org openssl rsa -in server.key.org -out server.key

    Generate self signed certificate
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
'''

ssl_enable = True
#Edit this path to point to your certificates
cert_dir = '/home/youruser/git/AmazonEcho/cert/'

def run(app):
    try:
        if ssl_enable:
            app.run(debug=True,
                    port=443,
                    threaded=True,
                    use_reloader=False,
                    use_debugger=True,
                    ssl_context=(cert_dir+'server.crt', 
                                 cert_dir+'server.key'),
                    host='0.0.0.0'
                    )
        else:
            app.run(debug=True,
                port=443,
                threaded=True,
                use_reloader=False,
                use_debugger=True,
                host='0.0.0.0'
                )
    finally:
        print "Disconnecting clients"
    print "Done"
