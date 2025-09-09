import { Form } from "@/components/composed_ui/Form";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { SignUpForm } from "@/components/composed_ui/SignUp";
import { Link } from "react-router-dom";
import { useEffect } from "react";
import { useAuthContext } from "@/hooks/useAuthContext";
import { useSignUpMutate } from "@/hooks/useSignUpMutate";

enum Role {
  Startup = "1",
  Investor = "2",
}

const passwordRequirements =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/;

const signUpSchema = z
  .object({
    first_name: z.string().nonempty("Не ввели ім’я").trim(),
    last_name: z.string().nonempty("Не ввели прізвище").trim(),
    username: z.string().nonempty("Не ввели ім’я користувача").trim(),
    email: z
      .string()
      .email("Введіть адресу електронної пошти у форматі name@example.com")
      .trim(),
    password: z
      .string()
      .min(8, "Пароль повинен містити щонайменше 8 символів")
      .regex(
        passwordRequirements,
        "Пароль має містити велику літеру, малу літеру, цифру та спеціальний символ"
      ),
    confirm_password: z
      .string()
      .min(8, "Пароль повинен містити щонайменше 8 символів")
      .regex(
        passwordRequirements,
        "Пароль має містити велику літеру, малу літеру, цифру та спеціальний символ"
      ),
    role: z.enum(Role, {
      error: "Виберіть кого ви представляєте",
    }),
    company_name: z.string().nonempty("Введiть назву компанiї.").trim(),
  })
  .superRefine(({ confirm_password, password }, ctx) => {
    if (confirm_password !== password) {
      ctx.addIssue({
        code: "custom",
        message: "Паролі не співпадають.",
        path: ["confirm_password"],
      });
      ctx.addIssue({
        code: "custom",
        message: "Паролі не співпадають.",
        path: ["password"],
      });
    }
  });

export type SignUpFormValues = z.infer<typeof signUpSchema>;

export function SignUp() {
  const auth = useAuthContext();
  const signUp = useSignUpMutate();
  const form = useForm<SignUpFormValues>({
    resolver: zodResolver(signUpSchema),
    mode: "onChange",
    defaultValues: {
      email: "",
      password: "",
      confirm_password: "",
      first_name: "",
      last_name: "",
      username: "",
      role: undefined,
      company_name: "",
    },
  });

  const { isValid, isSubmitting } = form.formState;

  const handleSignUp = async (data: SignUpFormValues) => {
    try {
      await signUp.mutateAsync(data);
    } catch (error: unknown) {
      if (typeof error === "object" && error !== null) {
        if ("username" in error) {
          form.setError("username", {
            type: "manual",
            message: "Це ім’я користувача вже використовується.",
          });
        }
        if ("email" in error) {
          form.setError("email", {
            type: "manual",
            message: "Ця електронна пошта вже використовується.",
          });
        }
        if ("role" in error) {
          form.setError("role", {
            type: "manual",
            message: "Виберіть роль, яку ви представляєте.",
          });
        }
        if ("password" in error) {
          form.setError("password", {
            type: "manual",
            message: "Пароль має містити велику літеру, малу літеру, цифру та спеціальний символ та бути не менше 8 символів.",
          });
        }
        return;
      }
      form.setError("root", {
        type: "manual",
        message: error instanceof Error ? error.message : "Невідома помилка",
      });
    }
  };

  useEffect(() => {
    if (auth?.user) {
      // TODO: navigate to user profile or dashboard when route available
    }
  }, [auth?.user]);

  return (
    <div className="mx-auto flex items-center justify-center h-screen">
      <div className="flex flex-col gap-6">
        <Form form={form} onSubmit={handleSignUp}>
          <Form.Header title="Реєстрація" />
          <Form.Body>
            <SignUpForm form={form} />
          </Form.Body>
          <Form.Footer>
            <Button disabled={!isValid || isSubmitting}>Зареєструватися</Button>
          </Form.Footer>
        </Form>
        <div className="flex items-center justify-center gap-1.5">
          <p className="text-center text-sm">Ви вже зареєстровані у нас?</p>
          <Button
            variant={"tertiary"}
            asChild
            className="font-display text-sm font-semibold hover:no-underline"
          >
            <Link to="/signin" className="underline">
              Увійти
            </Link>
          </Button>
        </div>
      </div>
    </div>
  );
}
