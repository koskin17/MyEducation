import { useMutation } from "@tanstack/react-query";
import type { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";
import {
  resetPassword,
  type RestorePasswordData,
  type RestorePasswordResponse,
} from "@/api/passwordRestore";

export function usePasswordRestoreMutate() {
  const navigate = useNavigate();
  return useMutation<
    RestorePasswordResponse,
    AxiosError<{ detail: string }>,
    RestorePasswordData
  >({
    mutationFn: resetPassword,
    onSuccess: () => {
      navigate("/password-restore-success");
    },
    onError: (error) => {
      if (error.response?.data.detail) {
        throw new Error(error.response.data.detail);
      }
      throw new Error(
        "Електронна пошта чи пароль вказані некоректно. Спробуйте ще раз."
      );
    },
  });
}
