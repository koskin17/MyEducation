import { useDesktop } from "@/hooks/useDesktop";
import { CraftMergeIcon } from "@/icons/CraftMergeIcon";
import { Link } from "react-router-dom";

export function Logo() {
  const isDesktop = useDesktop();

  return (
    <Link to="/" className="flex items-center gap-2.5">
      <CraftMergeIcon />
      {isDesktop && (
        <p className="font-display font-bold uppercase text-2xl text-main-black">
          StartHub
        </p>
      )}
    </Link>
  );
}
