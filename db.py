import pymysql.cursors


CONNECTION = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='pokedex',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)



cursor = CONNECTION.cursor()


