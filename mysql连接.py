from pymysql import *

def main():
    conn = connect(host='192.168.75.129',port=3306,database='day23',user='root',password='lr100312',charset='utf8')
    cs1 = conn.cursor()
    count = cs1.execute('insert into goods_cates(name) values("硬盘")')
    print(count)
    count = cs1.execute('insert into goods_cates(name) values("光盘")')
    print(count)
    conn.commit()
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()
