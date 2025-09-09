import { Link } from "react-router-dom";
import { Button } from "../ui/button";
import { useAuthContext } from "@/hooks/useAuthContext";
import { AvatarIcon } from "@/icons/AvatarIcon";

export function AuthButtons() {
  const auth = useAuthContext();
  return (
    <div className="flex items-center gap-6">
      {auth.user ? (
        <Button variant="tertiary" asChild>
          <span className="flex items-center gap-1.5">
            <AvatarIcon />
            <Link to="/profile">Мій профіль</Link>
          </span>
        </Button>
      ) : (
        <>
          <Button variant="tertiary" asChild>
            <Link to="/signin">Увійти</Link>
          </Button>
          <Button>
            <Link to="/signup">Зареєструватися</Link>
          </Button>
        </>
      )}
    </div>
  );
}
