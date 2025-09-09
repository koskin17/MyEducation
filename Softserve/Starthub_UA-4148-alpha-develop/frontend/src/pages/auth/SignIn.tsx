import { Form } from "@/components/composed_ui/Form";
import { SignInForm } from "@/components/composed_ui/SignIn";
import { Button } from "@/components/ui/button";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { useSignInMutate } from "@/hooks/useSignInMutate";
import { useAuthContext } from "@/hooks/useAuthContext";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const signInSchema = z.object({
  email: z
    .string()
    .email("Введіть адресу електронної пошти у форматі name@example.com"),
  password: z.string().min(6, "Електронна пошта чи пароль вказані некоректно"),
});

export type SignInFormValues = z.infer<typeof signInSchema>;

export function SignIn() {
  const navigate = useNavigate();
  const auth = useAuthContext();
  const signIn = useSignInMutate();
  const form = useForm<SignInFormValues>({
    resolver: zodResolver(signInSchema),
    mode: "onChange",
    defaultValues: {
      email: "",
      password: "",
    },
  });

  useEffect(() => {
    if (auth?.user) {
      navigate("/enterprises-and-industries");
    }
  }, [auth?.user]);

  const { isValid, isSubmitting } = form.formState;

  const handleSignIn = async (data: SignInFormValues) => {
    try {
      await signIn.mutateAsync(data);
    } catch (error: unknown) {
      form.setError("password", {
        type: "manual",
        message: error instanceof Error ? error.message : "Невідома помилка",
      });
    }
  };

  return (
    <div className="px-2 mx-auto flex items-center justify-center h-screen">
      <div className="flex flex-1 flex-col gap-6 items-center">
        <Form form={form} onSubmit={handleSignIn}>
          <Form.Header title="Вхід на платформу" />
          <Form.Body>
            <SignInForm form={form} />
          </Form.Body>
          <Form.Footer>
            <Button disabled={!isValid || isSubmitting}>Увійти</Button>
          </Form.Footer>
        </Form>
        <div className="font-display text-sm">
          <span>Вперше на нашому сайті?</span>{" "}
          {/* TODO: Link tag with to attribute and signup value */}
          <Button variant={'tertiary'} className="underline font-semibold">
            Зареєструйтесь
          </Button>
        </div>
      </div>
    </div>
  );
}
