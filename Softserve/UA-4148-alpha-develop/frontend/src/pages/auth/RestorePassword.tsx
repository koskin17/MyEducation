import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { Form } from "@/components/composed_ui/Form";
import { RestorePasswordForm } from "@/components/composed_ui/RestorePassword";
import { Button } from "@/components/ui/button";
import { Link, useSearchParams } from "react-router-dom";
import { useEffect } from "react";
import { useValidToken } from "@/hooks/useValidToken";
import { usePasswordRestoreMutate } from "@/hooks/usePasswordRestoreMutate";

const passwordRequirements =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/;

const restorePasswordSchema = z
  .object({
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
  })
  .refine((data) => data.password === data.confirm_password, {
    message: "Паролі не співпадають.",
    path: ["confirm_password"],
  });
export type RestorePasswordFormValues = z.infer<typeof restorePasswordSchema>;

export function RestorePassword() {
  const restorePassword = usePasswordRestoreMutate();
  const restoreTokenValidQuery = useValidToken();
  const [params] = useSearchParams();
  const form = useForm<RestorePasswordFormValues>({
    resolver: zodResolver(restorePasswordSchema),
    mode: "onChange",
    defaultValues: {
      password: "",
      confirm_password: "",
    },
  });

  const { isValid, isSubmitting } = form.formState;
  const token = params.get("token");

  const handleRestorePassword = async (data: RestorePasswordFormValues) => {
    if (!token) return;
    try {
      await restorePassword.mutateAsync({
        ...data,
        token,
      });
    } catch (error: unknown) {
      form.setError("confirm_password", {
        type: "manual",
        message: error instanceof Error ? error.message : "Невідома помилка",
      });
    }
  };

  useEffect(() => {
    if (token) {
      restoreTokenValidQuery.mutate({
        token,
      });
    }
  }, []);

  return (
    <div className="px-2 mx-auto flex items-center justify-center h-screen">
      <div className="flex flex-col gap-6">
        <Form form={form} onSubmit={handleRestorePassword}>
          <Form.Header title="Відновлення паролю" />
          <Form.Body>
            <RestorePasswordForm form={form} />
          </Form.Body>
          <Form.Footer>
            <Button disabled={!isValid || isSubmitting}>Зберегти пароль</Button>
          </Form.Footer>
        </Form>
        <Button
          variant={"tertiary"}
          asChild
          className="font-display text-sm font-semibold hover:no-underline"
        >
          <Link to="/signin" className="underline">
            Повернутися до входу
          </Link>
        </Button>
      </div>
    </div>
  );
}
