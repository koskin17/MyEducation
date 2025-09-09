import { Form } from "@/components/composed_ui/Form";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { ForgotPasswordForm } from "@/components/composed_ui/ForgotPassword";
import { Link } from "react-router-dom";
import { useForgotPasswordMutate } from "@/hooks/useForgotPasswordMutate";

const forgotPasswordSchema = z.object({
  email: z
    .string()
    .email("Введіть адресу електронної пошти у форматі name@example.com"),
});

export type ForgotPasswordFormValues = z.infer<typeof forgotPasswordSchema>;

export function ForgotPassword() {
  const forgotPassword = useForgotPasswordMutate();
  const form = useForm<ForgotPasswordFormValues>({
    resolver: zodResolver(forgotPasswordSchema),
    mode: "onChange",
    defaultValues: {
      email: "",
    },
  });

  const { isValid, isSubmitting } = form.formState;

  const handleForgotPassword = async (data: ForgotPasswordFormValues) => {
    try {
      await forgotPassword.mutateAsync(data);
    } catch (error: unknown) {
      form.setError("email", {
        type: "manual",
        message: error instanceof Error ? error.message : "Невідома помилка",
      });
    }
  };

  return (
    <div className="px-2 mx-auto flex items-center justify-center h-screen">
      <div className="flex flex-1 flex-col gap-6 items-center">
        <Form form={form} onSubmit={handleForgotPassword}>
          <Form.Header title="Забули пароль?" />
          <Form.Body>
            <ForgotPasswordForm form={form} />
          </Form.Body>
          <Form.Footer>
            <Button disabled={!isValid || isSubmitting}>
              Відновити пароль
            </Button>
          </Form.Footer>
        </Form>
        <div className="font-display text-sm">
          <span>Я згадав свій пароль.</span>{" "}
          <Link to="/signin" className="underline font-semibold">
            Повернутися до входу
          </Link>
        </div>
      </div>
    </div>
  );
}
