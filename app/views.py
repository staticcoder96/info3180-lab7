"""

Flask Documentation:     http://flask.pocoo.org/docs/

Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/

Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.

"""



from app import app

from flask import render_template, request, redirect, url_for, flash,jsonify,make_response

from bs4 import BeautifulSoup

import requests

import urlparse

import image_getter



###

# Routing for your application.

###



@app.route('/')

def home():

    """Render website's home page."""

    return render_template('home.html')

    

@app.route("/api/thumbnails", methods = ["GET","POST"])

def thumbs():

    if request.method == "POST":

        #urls= image_getter.URLs()

        null = None

        stuff={

            "error": null,

            "message": "Success",

            "thumbnails":

                [

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-ebd7/k2-_c26840ed-0ac3-478d-9173-398eaa1faef2.v1.png-735f1c435683f1593e165daeb4e59484247556ee-crushed-1x1.png",

                    "https://i5.walmartimages.com/asr/6f72b560-cf7f-4efe-8ffc-2d4723fd6f02_1.03da0f6f9ab6313230c1009c91c5d05c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",

                    "https://i5.walmartimages.com/asr/6f72b560-cf7f-4efe-8ffc-2d4723fd6f02_1.03da0f6f9ab6313230c1009c91c5d05c.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF",

                    "https://www.walmart.com/static/img/clear.png?action=p13_start&timestamp=1490078568839&page=Product&placementId=Product-m3&bstc=undefined",

                    "https://i5.walmartimages.com/asr/f360c04f-aa37-43bb-b74c-d260bdd3c56e_1.0161a0cdf3393a67e29b7c9664ca1d0d.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/0466f895-ebd1-476c-a45b-4f285f14a1f3_1.e7b3341630ecc546acad2871911307a8.png?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/d677fd13-93c7-4256-884a-c58257d8310f_1.d7d64d0a46217e666283e66f6ee4e1b0.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/91849581-2b83-4664-9233-82a8a553b304_1.b4a2fa46636b89c487f463a7095b2565.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/6cb6666a-189f-459b-ab37-6d850313f8dd_1.a2199672581eaed34e4e0c29a3ef3894.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/29cd259b-8b7e-466c-98a3-d4ce3d514c7e_1.0d5795d0fead1abe4ec898af6d05ce74.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/75ce7645-424c-4eda-9988-fd6845111d4d_1.6c0458ab475198583f30e8d808d67f33.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/691e1f61-34ce-4f61-b70e-f44a54476b25_1.06e9e286d0148ee62d7f4aa8c3437e57.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://www.walmart.com/static/img/clear.png?action=p13_end&timestamp=1490078568938&page=Product&placementId=Product-m3&bstc=undefined",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/walmart%3Aroku.png",

                    "https://www.walmart.com/static/img/clear.png?action=p13_start&timestamp=1490078568839&page=Product&placementId=Product-b1&bstc=undefined",

                    "https://i5.walmartimages.com/asr/dd648f0a-edab-4c62-9157-051e2c73637b_1.d5bb911ec2c08224787e328e0ac7ff34.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/0ac06c03-f851-4593-84ef-5e21d1460f3d_1.6fb25d21733810bd8e3439a4bb421d54.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/d1127ff4-f437-459d-9503-2cbde415d7ef_1.62c03c6b7798f7e9eac2c450047221f6.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/4ab87698-c642-4298-9ecb-f43bc5dce23a_1.8098f6cf872c9abdb04c31d2881698e6.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/8289d1b0-b630-46bc-a33e-f0e5b347ff70_1.f06710f6452b38a99f478c87c8b87936.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",
                    "https://i5.walmartimages.com/asr/93e90eef-6ff9-4ee4-b5b1-692d967450cb_1.07efa1290b82f3b4f50b95c09a9b3464.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/d46e2aa0-7bc5-4e54-b9ab-1020bef0c9b5_1.4b0b4479e8e6fdf38c9b33a00f98788b.jpeg?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://i5.walmartimages.com/asr/3d62c34c-5c65-40b0-ab2d-a6555895779d_1.f34bda5c97b5d316ad4f49d79ccdd849.png?odnWidth=144&odnHeight=144&odnBg=ffffff",

                    "https://www.walmart.com/static/img/clear.png?action=p13_end&timestamp=1490078568938&page=Product&placementId=Product-b1&bstc=undefined",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-d0f2/k2-_c379cb69-17f1-44da-89ba-53ea082853c5.v11.png-d4b66ddbfe95500ed27934e3f401aae8c3c30f74-crushed-70x65.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-a9e8/k2-_84280275-d251-461d-b29f-456506a3ec98.v11.png-56e11fae4af0df6777aaf267111aecad7f732698-crushed-70x65.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-e2f5/k2-_7feabc9d-72da-4dda-8af2-56bba05ab4ad.v11.png-08c9161116502a45df08cb62b05bb588b43ccfb7-crushed-70x65.png",

                    "https://ll-us-i5.wal.co/dfw/63fd9f59-579f/k2-_e1ee901c-814c-4326-ab2d-4056d02e9d5b.v11.png-b8bd30a9336f729a293f34915f0a2ba4b028b6af-crushed-70x65.png"

                    ]

                    }

        return jsonify(stuff)


@app.route("/thumbnails/view")
def showImages():
   urls= image_getter.URLs()
   return render_template("thumbnails.html",urls=urls)


###

# The functions below should be applicable to all Flask apps.

###



@app.route('/<file_name>.txt')

def send_text_file(file_name):

    """Send your static text file."""

    file_dot_text = file_name + '.txt'

    return app.send_static_file(file_dot_text)





@app.after_request

def add_header(response):

    """

    Add headers to both force latest IE rendering engine or Chrome Frame,

    and also to tell the browser not to cache the rendered page.

    """

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'

    response.headers['Cache-Control'] = 'public, max-age=0'

    return response





@app.errorhandler(404)

def page_not_found(error):

    """Custom 404 page."""

    return render_template('404.html'), 404





if __name__ == '__main__':

    app.run(debug=True,host="0.0.0.0",port="8080")