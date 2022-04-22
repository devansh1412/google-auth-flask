from sqlalchemy.sql import text
from model import SQLALCHEMY_DATABASE_URI

# IMPORT THE REQUIRED LIBRARY
import sqlalchemy as db
 
# DEFINE THE ENGINE (CONNECTION OBJECT)
engine = db.create_engine(SQLALCHEMY_DATABASE_URI)

def get_topic_frequency_data():
    topic_dict = dict()
    try:
        sql = text("SELECT tags "+
                    "FROM blog "+
                    "WHERE status = 'A' ")
        results = engine.execute(sql)
        for item in results:
            for tags in item.tags:
                if tags in topic_dict.keys():
                    topic_dict[tags] += 1
                else:
                    topic_dict[tags] = 1
        print(topic_dict)
        return topic_dict
    except Exception as e:
        print(str(e))
        return []

def store_topic_frequency_data():
    return

def get_company_selection_frequency_data() -> list:
    try:
        sql = text("SELECT company.name, COUNT(*) as frequency " + 
                "FROM company INNER JOIN user_company_blog " +
                "ON company.id = user_company_blog.company_id " +
                "WHERE selected = 'true' and company.status = 'A' " +
                "GROUP BY company.name " +
                "ORDER BY frequency desc " + 
                "LIMIT 10")
        results = engine.execute(sql)
        company_frequency_list = list()
        for item in results:
            row = item._asdict()
            company_frequency_list.append(row)
        print(company_frequency_list)
        return company_frequency_list
    except Exception as e:
        print(str(e))
        return []

def store_company_selection_frequency_data():
    return
    
def get_cgpa_company_data():
    try:
        sql = text("SELECT company.name, avg(user_table.cgpa) as average_cgpa " +
                    "FROM company " + 
                    "INNER JOIN user_company_blog ON company.id = user_company_blog.company_id " +
                    "INNER JOIN user_table ON user_company_blog.user_id = user_table.id " +
                    "WHERE user_company_blog.selected = 'true' and user_company_blog.status = 'A' " +
                    "GROUP BY company.name " +
                    "LIMIT 10")
        results = engine.execute(sql)
        average_cgpa_list = list()
        for item in results:
            row = item._asdict()
            average_cgpa_list.append(row)
        print(average_cgpa_list)
        return average_cgpa_list
    except Exception as e:
        print(str(e))
        return []

def store_cgpa_company_data():
    return

def get_difficulty_level_data():
    try:
        sql = text("SELECT level ,COUNT(*) " +
                    "FROM blog " +
                    "WHERE status = 'A' " +
                    "GROUP BY level")
        results = engine.execute(sql)
        difficulty_level_list = list()
        for item in results:
            row = item._asdict()
            difficulty_level_list.append(row)
        print(difficulty_level_list)
        return difficulty_level_list
    except Exception as e:
        print(str(e))
        return []

def store_difficulty_level_data():
    return


# if __name__ == "__main__":
#     get_company_selection_frequency_data()
#     get_cgpa_company_data()
#     get_difficulty_level_data()
#     get_topic_frequency_data()