import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { Input } from "../ui/input";
import type { UseFormReturn } from "react-hook-form";
import type { ForgotPasswordFormValues } from "@/pages/auth/ForgotPassword";

interface ForgotPasswordFormProps {
  form: UseFormReturn<ForgotPasswordFormValues>;
}

export function ForgotPasswordForm({ form }: ForgotPasswordFormProps) {
  return (
    <div className="flex flex-col gap-6">
      <p>
        Введіть електронну адресу вказану при реєстрації для відновлення паролю.
        <br />
        На зазначену вами електронну пошту буде відправлено листа з посиланням
        для відновлення паролю.
      </p>
      <FormField
        control={form.control}
        name="email"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel>Електронна пошта</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-sm flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть свою електронну пошту"
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
