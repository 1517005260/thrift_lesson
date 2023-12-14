namespace cpp match_service  ##使用c++，并且该接口名字为match_service


struct User   ##存储传入match服务的用户数据，以thrift格式
{
    1: i32 id,   ##以编号开头，i32表示int，以逗号分隔
    2: string name,
    3: i32 score  ##匹配实力相近的人
}


service Match   ##函数接口，习惯命名大写
{
    i32 add_user(1: User user , 2: string info),
    ##函数返回int，用于给匹配服务增加用户，传参有编号，类型+变量名

    i32 remove_user(1: User user , 2: string info),
}
