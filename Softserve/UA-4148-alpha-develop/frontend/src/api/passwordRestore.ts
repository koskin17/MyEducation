import axios from "./index";

export interface RestorePasswordData {
  token: string;
  password: string;
  confirm_password: string;
}

export interface RestorePasswordResponse {
  detail?: string
}

export async function resetPassword(data: RestorePasswordData): Promise<RestorePasswordResponse> {
  const response = await axios.post<RestorePasswordResponse>("/users/reset-password/", data);
  return response.data;
}
