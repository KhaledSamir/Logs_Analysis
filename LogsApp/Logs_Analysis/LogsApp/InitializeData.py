import psycopg2


viewQuery = '''create view articleView as 
            Select ar.title , ar.slug , count(path) as Views , ar.author from log 
            Join articles ar 
            on log.path like concat('%' , ar.slug) 
            Group by ar.title , ar.slug , ar.author
            Order by count(path) desc'''


def InitializeDB():
    db = psycopg2.connect('dbname=news')
    c = db.cursor()
    c.execute(viewQuery)
    c.close()
    return 'View created!'
    
print(InitializeDB())



