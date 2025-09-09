import { signUp, type SignUpData, type SignUpResponse } from "@/api/auth";
import { useMutation } from "@tanstack/react-query";
import type { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";

export function useSignUpMutate() {
  const navigate = useNavigate();
  return useMutation<
    SignUpResponse,
    AxiosError,
    SignUpData
  >({
    mutationFn: signUp,
    onSuccess: () => {
      navigate("/signin");
    },
    onError: (error) => {
      console.log(error);
      if (error.status && error.status >= 500) {
        throw new Error("Серверна помилка, спробуйте пізніше");
      }
      if (error.response?.data) {
        throw error.response?.data
      }
      throw new Error(
        "Електронна пошта чи пароль вказані некоректно. Спробуйте ще раз."
      );
    },
  });
}
