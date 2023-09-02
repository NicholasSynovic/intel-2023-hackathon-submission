from pandas import DataFrame

def main()  ->  None:
    users: dict = {"Username": ["user"], "Password": ["password"]}

    usersDF: DataFrame = DataFrame(data=users)

    usersDF.to_json(path_or_buf="users.json", index=True, indent=4)

if __name__ == "__main__":
    main()
