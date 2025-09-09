import { Heart } from "lucide-react";
import { Button } from "../ui/button";
import { useAuthContext } from "@/hooks/useAuthContext";
import { useSubscribeStartup } from "@/hooks/useSubscribeStartup";

interface SubscribeStartupButtonProps {
  id: number;
}

const SubscribeStartupButton = ({ id }: SubscribeStartupButtonProps) => {
  const mutate = useSubscribeStartup();
  const { user } = useAuthContext();
  const handleSubscribe = async () => {
    mutate.mutateAsync({ startupId: id });
  };

  if (user?.role != "investor") {
    return;
  }

  // TODO: check if investor subscribed for this startup
  const subscribed = true;
  return (
    <Button disabled={mutate.isPending} variant={"tertiary"} onClick={handleSubscribe}>
      {subscribed ? <Heart className="fill-black" /> : <Heart />}
    </Button>
  );
};

export default SubscribeStartupButton;
