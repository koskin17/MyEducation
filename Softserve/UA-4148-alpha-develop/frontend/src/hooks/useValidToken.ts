import {
  validateTokenRestorePassword,
  type RestoreTokenData,
  type RestoreTokenResponse,
} from "@/api/validateTokenRestorePassword";
import { useMutation } from "@tanstack/react-query";
import type { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";

export function useValidToken() {
  const navigate = useNavigate();
  return useMutation<
    RestoreTokenResponse,
    AxiosError<{ detail: string }>,
    RestoreTokenData
  >({
    mutationFn: validateTokenRestorePassword,
    onSuccess: (data) => {
      if (!data.valid) {
        navigate("/forgot-password");
        return;
      }
    },
    onError: (error) => {
      console.error(error);
      if (error.status === 400) {
        navigate("/forgot-password");
      }
      if (error.response?.status === 500) {
        throw new Error("Серверна помилка, спробуйте пізніше");
      }
      throw new Error("Щось пішло не так, спробуйте ще раз");
    },
  });
}
