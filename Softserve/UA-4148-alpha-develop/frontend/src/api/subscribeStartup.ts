import axios from "./index";

export interface SubscribeStartupData {
  startupId: number;
}

export interface SubscribeStartupResponse {
  message?: string;
}

export async function subscribeStartup(
  data: SubscribeStartupData
): Promise<SubscribeStartupResponse> {
  const response = await axios.post<SubscribeStartupResponse>(
    `/projects/${data.startupId}/subscribe/`
  );
  return response.data;
}
