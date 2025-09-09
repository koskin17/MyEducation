import { useMutation } from "@tanstack/react-query";
import type { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";
import { forgotPassword, type ResetPasswordData, type ResetPasswordResponse } from "@/api/forgot-password";

export function useForgotPasswordMutate() {
  const navigate = useNavigate();
  return useMutation<
    ResetPasswordResponse,
    AxiosError<{ email: string[] }>,
    ResetPasswordData
  >({
    mutationFn: forgotPassword,
    onSuccess: () => {
      navigate("/password-recovery-email-sent");
    },
    onError: (error) => {
      console.error(error);
      if (error.response?.data?.email) {
        throw new Error("Введіть адресу електронної пошти у форматі name@example.com");
      }
      if (error.response?.status === 500) {
        throw new Error("Серверна помилка, спробуйте пізніше");
      }
      throw new Error("Зазначена електронна адреса не зареєстрована");
    },
  });
}
