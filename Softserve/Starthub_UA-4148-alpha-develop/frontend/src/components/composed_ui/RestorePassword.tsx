import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import type { UseFormReturn } from "react-hook-form";
import type { RestorePasswordFormValues } from "@/pages/auth/RestorePassword";
import { PasswordInput } from "../composed/PasswordInput";

interface RestorePasswordFormProps {
  form: UseFormReturn<RestorePasswordFormValues>;
}

export function RestorePasswordForm({ form }: RestorePasswordFormProps) {
  return (
    <div className="flex flex-col gap-6">
      <FormField
        control={form.control}
        name="password"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel>Новий пароль</FormLabel>
            <p className="font-display text-[10px] text-main-gray-90">
              Пароль повинен мати 8+ символів, містити принаймні велику, малу
              літеру (A..Z, a..z) та цифру (0..9).
            </p>
            <FormControl>
              <PasswordInput
                className="shadow-none border border-inactive-100 rounded-sm flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть пароль"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="confirm_password"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel>Повторіть новий пароль</FormLabel>
            <FormControl>
              <PasswordInput
                className="shadow-none border border-inactive-100 rounded-sm flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Повторіть введений пароль"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
    </div>
  );
}
