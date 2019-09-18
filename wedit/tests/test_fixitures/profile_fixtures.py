query_get_profiles = '''
    query {
        users {
            email
            username
        }
    }
'''

query_get_user_profile = '''
    query {{
        user(email:"{}") {{
            email
            username
        }}
    }}
'''

query_users_with_invalid_arguments = '''
    query {{
        users(errors: "{}") {{
            email
            username
        }}
    }}
'''


user_login_mutation = '''
    mutation{{
        login(email:"{}",password:"{}") {{
            token
        }}
    }}
'''

create_profile_mutation = '''
mutation {{
  createUser(email:"{}",username:"{}",firstName:"{}", lastName:"{}", password:"{}") {{
    email
    username
    firstName
    lastName
    password
  }}
}}
'''
