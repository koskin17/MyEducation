import type { PropsWithChildren } from "react";
import type { FieldValues, UseFormReturn } from "react-hook-form";
import { Form as FormComponent } from "@/components/ui/form";

interface FormProps<T extends FieldValues> {
  form: UseFormReturn<T>;
  onSubmit: (data: T) => void;
  children: React.ReactNode;
}

export function Form<T extends FieldValues>({
  form,
  onSubmit,
  children,
}: FormProps<T> & PropsWithChildren) {
  return (
    <FormComponent {...form} >
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="bg-white rounded-md overflow-hidden max-w-[572px] w-full"
      >
        {children}
      </form>
    </FormComponent>
  );
}

interface FormHeaderProps {
  title: string;
}

function FormHeader({ title }: FormHeaderProps) {
  return (
    <div className="py-4 px-6 border-b border-inactive-60">
      <h2 className="font-display font-semibold">{title}</h2>
    </div>
  );
}

FormHeader.displayName = "Form.Header";

function FormBody({ children }: PropsWithChildren) {
  return <div className="p-6 border-b border-inactive-60">{children}</div>;
}

FormBody.displayName = "Form.Body";

function FormFooter({ children }: PropsWithChildren) {
  return <div className="py-4 px-6">{children}</div>;
}

FormFooter.displayName = "Form.Footer";

Form.Header = FormHeader;
Form.Body = FormBody;
Form.Footer = FormFooter;
