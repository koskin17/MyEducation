import { Form } from "@/components/composed_ui/Form";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

export function PasswordRestoreSuccess() {
  return (
    <div className="px-2 mx-auto flex items-center justify-center h-screen">
      <div className="bg-white rounded-md overflow-hidden max-w-[572px] w-full">
        <Form.Header title="Пароль збережено" />
        <Form.Body>
          <p className="font-display text-sm text-main-gray-90">
            Ваш новий пароль успішно збережено
          </p>
        </Form.Body>
        <Form.Footer>
          <Button asChild>
            <Link to="/signin">Повернутися до входу</Link>
          </Button>
        </Form.Footer>
      </div>
    </div>
  );
}
