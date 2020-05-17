from google.cloud import talent_v4beta1

GOOGLE_APPLICATION_CREDENTIALS = {
  "type": "service_account",
  "project_id": "resumatch-277502",
  "private_key_id": "58e1a4618baa5e6be2c89cdfc9ca48dcea25ca8e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBz7LG2dMiTpbJ\ncbNjzTjdLAM2Pg/GeAM9/bF9zBv7qdPMtrW6op5+DHw0IHhbwOVNoowAkOonPYIv\nB9HfbECoM+Tzf7KPYLa07O4hwL480eRvDK4whaiLZRLZhL2OPceo5ax1eTdhJDjg\nyMa9FZkEac9BnRZeyrA+yOh1ERJymvvk+/MZ0rPZyY/WeB3QM1yJ9YIS84GhKKl/\nkzJA7sU+vLxLpscXqJX1g0HW9x06Rti74Z0w56mzsINJMNKIBLFm66Mkuqm7/Xz+\nC7+ZbESXePTL8rDt0pxUwUiTVztjY3blB8rC7r5PVB5j7/v42vXDOyL54MR4OVrU\nN0SHtyyvAgMBAAECggEAUN2I0ehT7FYPGykKOOOJTNsO0gSOD3jGnYhrFLpjmJsw\n6JL5e1BbwesSras4nMv8wOpH8PqGAG5tEZN5MXgY+DWC20hWJ/Wp9g5/g2zI01ae\nMemACnXSL6sx9LkqYB2N335I+VDk1u7Gnp+XMJDA4jMFy3IwQcffRqsMNsAzSsZ+\nuY4oI5Qcck0oDUjE8X7iwE+XeFoZsAy01UVVX4BmChTvI8TVFR1Mt2AABO4AMQli\nUQaaXGftlCPZnM3935WVGzJmV+YtBm6VykjrkUkwWYmuOLT0f6el6fBKIhkbMkEU\nEdlOxzoXQTDfTtDEjms4V1UrR6keG4akUqErpaBRMQKBgQDn0wMwVisjZUhLhqkO\n4RfhsS2dSUj4kIH9ZgB5KNDVKz0Iuf/eu9mhECnEWJOn3So3l1Ivmv7jrHxwooDJ\nTpWZZMgGwZWU8jXPqAetEs9j8JYRdEl6g7GGsF83bVfX1lCsoy57m4NKEDpTXoHK\nHQZ4bwVbVdz0rxB7PJodUUFNfwKBgQDWBdu9ynQnB7U1cNNgdMGvs/YhUFVmxA5+\nW3PBu3L0OUZdxf7PI0gWvO1O6xOo+epuf/BpDxflwDA7aEK6XgVsOzIouwyoCH7E\nqaeAg4HDixEVIquVevJeDBf+cuZWh6B2bifjYMNt4xSG5Fgl/GStKerBlJK8DJ2M\nkmidlV0Y0QKBgD0JQrKsTUlRdlpkRwii3S3P/2mFDRBcw8za2U8NHwaxDq3IgwS6\nws70OXr3s1CkG2Rtk/bywR9in5TsRCo8ZYjwjvWwbFi9+MsGu5am+DGg+3H3Aw2d\ntNT4hOlMAa/TPoRlpmxnAocyhJjErjlvsO9uk6N7lORbX2SDDTSg2yezAoGBAJfr\nYKe/5eMunXpptCFrv3CxFa1gEL75vDAFSo3iOR8S6Nf3i4ANU0aQpQK36ySvAbGe\nL1Dj3drAKXyB7ZvM0ZyaCGjRHZLJNPL0Wmnm712WgXG3QoTA2PnZK876UHZrn4Nx\nfe7w6Mg/wHpf7BJKrkwczP7ML7w8WDlIU+pH8+WBAoGAU/Cy+Sg130GHu3Y+boAj\nP0br7lRkoua9HvRzoINRy/UE8ClwTkm/640rEByvH2j00LvgOEDyO4kLPSRYXcCS\nX9/I5KOBYzoBpavorLLa8ozf4x3KR1NDichGZs+DNccx9wCOjoP9It19cfnTFEVr\nDdIjVW77wVNlyd4M4Or9nYc=\n-----END PRIVATE KEY-----\n",
  "client_email": "resumatch@resumatch-277502.iam.gserviceaccount.com",
  "client_id": "100951337452385806242",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/resumatch%40resumatch-277502.iam.gserviceaccount.com"
}


client = talent_v4beta1.JobServiceClient(credentials=GOOGLE_APPLICATION_CREDENTIALS)

parent = client.project_path("resumatch")
request_metadata = {
    "before_request": 0
}

for page in client.search_jobs(parent, request_metadata).pages:
    print(page)