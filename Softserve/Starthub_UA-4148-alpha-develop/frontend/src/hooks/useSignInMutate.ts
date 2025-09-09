import { useMutation } from "@tanstack/react-query";
import { signIn, type SignInData, type SignInResponse } from "../api/auth";
import { useAuthContext } from "./useAuthContext";
import type { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";

export function useSignInMutate() {
  const navigate = useNavigate();
  const auth = useAuthContext();
  return useMutation<
    SignInResponse,
    AxiosError<{ detail: string }>,
    SignInData
  >({
    mutationFn: signIn,
    onSuccess: (data) => {
      auth?.login(data);
      navigate("/enterprises-and-industries");
    },
    onError: (error) => {
      console.error(error);
      if (error.response?.data.detail == "Invalid credentials") {
        throw new Error(
          "Електронна пошта чи пароль вказані некоректно. Спробуйте ще раз."
        );
      }
      if (error.response?.status === 500) {
        throw new Error("Серверна помилка, спробуйте пізніше");
      }
      throw new Error(
        "Електронна пошта чи пароль вказані некоректно. Спробуйте ще раз."
      );
    },
  });
}
