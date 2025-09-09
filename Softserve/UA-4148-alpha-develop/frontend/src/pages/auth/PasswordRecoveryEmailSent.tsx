import { Form } from "@/components/composed_ui/Form";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

export function PasswordRecoveryEmailSent() {
  return (
    <div className="px-2 mx-auto flex items-center justify-center h-screen">
      <div className="bg-white rounded-md overflow-hidden max-w-[572px] w-full">
        <Form.Header title="Відновлення паролю майже завершено" />
        <Form.Body>
          <p className="font-display text-sm">
            На вашу електронну адресу були надіслані інструкції для зміни
            паролю.
          </p>
        </Form.Body>
        <Form.Footer>
          <Button asChild>
            <Link to="/signin">
              Повернутися до входу
            </Link>
          </Button>
        </Form.Footer>
      </div>
    </div>
  );
}
