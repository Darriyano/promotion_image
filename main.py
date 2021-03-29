from flask import Flask, url_for

app = Flask(__name__)



@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Планета</title>
                  </head>
                  <body>
                    <h1 align=center class="colorchanger">Жди нас, марс!</h1>
                    <br>
                    <img src="{url_for('static', filename='img/mars.jpg')}" width="450" height="450" alt="Mars pic!">
                    <div class="alert alert-dark" role="alert">
                    <h2>Человечество вырастает из дерева</h2> </div>
                    <div class="alert alert-success" role="alert">
                     <h2> Человечеству мала одна планета </h2>
                    </div>
                    <div class="alert alert-dark" role="alert">
                     <h2> Сделаем обитаемыми пока безжизненные планеты </h2>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h2> И начнём с Марса </h2>
                    </div>
                    <div class="alert alert-danger" role="alert">
                     <h2> Присоединяйся! </h2>
                    </div>
                  </body>
                </html>'''


def main():
    app.run(host='localhost', port=8080)


if __name__ == '__main__':
    main()
