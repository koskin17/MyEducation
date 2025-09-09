import { subscribeStartup } from "@/api/subscribeStartup";
import { useMutation } from "@tanstack/react-query";
import type { AxiosError } from "axios";
import { toast } from "sonner";

export function useSubscribeStartup() {
  return useMutation({
    mutationFn: subscribeStartup,
    onSuccess: () => {
      toast.success("Стартап успiщно збережений");
    },
    onError: (error: AxiosError) => {
      console.error(error);
      if (error?.response?.status === 500) {
        toast.error("Серверна помилка, спробуйте пізніше");
        return;
      }
      toast.error("Щось пішло не так, спробуйте ще раз");
    },
  });
}
