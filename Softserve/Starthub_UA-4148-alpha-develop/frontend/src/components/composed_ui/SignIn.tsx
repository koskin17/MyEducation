import { Button } from "@/components/ui/button";
import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { Input } from "../ui/input";
import type { UseFormReturn } from "react-hook-form";
import type { SignInFormValues } from "@/pages/auth/SignIn";
import { Link } from "react-router-dom";
import { PasswordInput } from "../composed/PasswordInput";

interface SignInFormProps {
  form: UseFormReturn<SignInFormValues>;
}

export function SignInForm({ form }: SignInFormProps) {
  return (
    <div className="flex flex-col gap-6">
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
      <div className="flex flex-col gap-2">
        <FormField
          control={form.control}
          name="password"
          render={({ field }) => (
            <FormItem className="gap-1">
              <FormLabel>Пароль</FormLabel>
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
        <Button variant={"tertiary"} className="self-end">
          <Link to="/forgot-password" className="text-sm">Забули пароль?</Link>
        </Button>
      </div>
    </div>
  );
}
