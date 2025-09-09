import axios from "./index";

export interface RestoreTokenData {
  token: string;
}

export interface RestoreTokenResponse {
  valid: boolean;
}

export async function validateTokenRestorePassword(
  data: RestoreTokenData
): Promise<RestoreTokenResponse> {
  const response = await axios.post<RestoreTokenResponse>(
    "/users/validate-reset-token/",
    data
  );
  return response.data;
}
