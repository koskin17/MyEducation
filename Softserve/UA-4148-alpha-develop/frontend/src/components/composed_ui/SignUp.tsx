import {
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";

import { Input } from "../ui/input";
import { type UseFormReturn } from "react-hook-form";
import type { SignUpFormValues } from "@/pages/auth/SignUp";
import { Checkbox } from "../ui/checkbox";
import { Link } from "react-router-dom";

interface SignUpFormProps {
  form: UseFormReturn<SignUpFormValues>;
}

export function SignUpForm({ form }: SignUpFormProps) {
  return (
    <div className="flex flex-col gap-6">
      <FormLabel required>Обов’язкові поля позначені зірочкою</FormLabel>
      <FormField
        control={form.control}
        name="email"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Електронна пошта</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть свою електронну пошту"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="password"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Пароль</FormLabel>
            <p className="font-display text-[10px] text-main-gray-90">
              Пароль повинен мати 8+ символів, містити принаймні велику, малу
              літеру (A..Z, a..z) та цифру (0..9).
            </p>
            <FormControl>
              {/* TODO: use PasswordInput after merge */}
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
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
            <FormLabel required>Повторiть пароль</FormLabel>
            <FormControl>
              {/* TODO: use PasswordInput after merge */}
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть пароль ще раз"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="last_name"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Прізвище</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть ваше прізвище"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="first_name"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Ім‘я</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть ваше ім’я"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="username"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Ім‘я користувача чатiв</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Введіть ім’я для чатiв"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <FormField
        control={form.control}
        name="role"
        render={({ field }) => {
          const roleValue = field.value;
          return (
            <FormItem className="gap-1">
              <FormLabel required>Кого ви представляєте?</FormLabel>
              <FormControl>
                <div className="ml-6 flex flex-col gap-2">
                  <div className="flex items-center gap-2">
                    <Checkbox
                      checked={roleValue === "1"}
                      onCheckedChange={() => field.onChange("1")}
                      {...field}
                    />
                    <span
                      onClick={() => field.onChange("1")}
                      className="text-sm cursor-pointer text-main-black-90 font-display font-light"
                    >
                      Стартап проєкт, який шукає інвестиції
                    </span>
                  </div>
                  <div className="flex items-center gap-2">
                    <Checkbox
                      checked={roleValue === "2"}
                      onCheckedChange={() => field.onChange("2")}
                    />
                    <span
                      onClick={() => field.onChange("2")}
                      className="text-sm cursor-pointer text-main-black-90 font-display font-light"
                    >
                      Iнвестор, який шукає cтартап
                    </span>
                  </div>
                </div>
              </FormControl>
              <FormMessage />
            </FormItem>
          );
        }}
      />
      <FormField
        control={form.control}
        name="company_name"
        render={({ field }) => (
          <FormItem className="gap-1">
            <FormLabel required>Назва компанiї</FormLabel>
            <FormControl>
              <Input
                className="shadow-none border border-inactive-100 rounded-xs flex focus-within:border-ring focus-within:ring-ring/50 focus-within:ring-[3px]"
                placeholder="Ввeдiть назву компанiї"
                {...field}
              />
            </FormControl>
            <FormMessage />
          </FormItem>
        )}
      />
      <p className="font-display text-sm text-main-black-90 font-light">
        Реєструючись, я погоджуюсь з {/* TODO: add terms-conditions route */}
        <Link className="font-semibold underline" to="/terms-conditions">
          правилами використання
        </Link>{" "}
        сайту StartupHub
      </p>
    </div>
  );
}
