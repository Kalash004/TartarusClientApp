from src.layers.Connector import Connector

if __name__ == "__main__":
    conn = Connector()
    # conn.delete("admin_users", 3)
    # print(conn.get_all("admin_users"))
    params = {
        "NAME": "Anton",
        "admin_id": "4"
    }
    print(conn.get_params("admin_users", params))
